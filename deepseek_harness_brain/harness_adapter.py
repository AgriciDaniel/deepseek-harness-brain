from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


INVENTORY_SCHEMA = "deepseek-harness.repository-inventory.v1"
PORTABILITY_SCHEMA = "deepseek-harness.portability-report.v1"
REQUIRED_ROOT_FILES = ("AGENTS.md", "package.json", "docs/architecture.md", "docs/testing.md", "vendor/README.md")
ALLOWED_PREFIXES = (
    ".agents/notes/implemented/",
    "apps/cli/tests/",
    "docs/",
    "examples/",
    "packages/",
    "vendor/",
)
ALLOWED_ROOT_FILES = {"AGENTS.md", "LICENSE", "README.md", "package.json", "pnpm-workspace.yaml"}


@dataclass(frozen=True)
class CheckoutFacts:
    root: Path
    commit: str
    version: str
    cordis_version: str
    tracked_dirty: bool
    paths: tuple[str, ...]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid JSON object: {path}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _safe_file(root: Path, relative: str) -> Path:
    candidate = root / relative
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root):
        if candidate.is_symlink():
            raise ValueError(f"refusing symlinked evidence path outside checkout: {relative}")
        raise ValueError(f"evidence path escapes checkout: {relative}")
    return resolved


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=False)


def _discover_paths(root: Path) -> tuple[str, ...]:
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink() and (relative in ALLOWED_ROOT_FILES or relative.startswith(ALLOWED_PREFIXES)):
            if not path.resolve().is_relative_to(root):
                raise ValueError(f"refusing symlinked evidence path outside checkout: {relative}")
    tracked = _git(root, "ls-files", "-z")
    if tracked.returncode == 0:
        candidates = [item for item in tracked.stdout.split("\0") if item]
    else:
        candidates = [path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()]
    allowed = []
    for relative in sorted(set(candidates)):
        if relative in ALLOWED_ROOT_FILES or relative.startswith(ALLOWED_PREFIXES):
            _safe_file(root, relative)
            allowed.append(relative)
    return tuple(allowed)


def inspect_checkout(checkout: Path, *, expected_commit: str | None = None) -> CheckoutFacts:
    root = checkout.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"checkout is not a directory: {root}")
    missing = [relative for relative in REQUIRED_ROOT_FILES if not _safe_file(root, relative).is_file()]
    if missing:
        raise ValueError("not a DeepSeek Harness checkout, missing: " + ", ".join(missing))
    package = _json_object(root / "package.json")
    if package.get("name") != "@deepseek-ai/dsh-root":
        raise ValueError("root package name is not @deepseek-ai/dsh-root")
    cordis_package = _json_object(root / "vendor" / "cordis" / "package.json")
    revision = _git(root, "rev-parse", "HEAD")
    commit = revision.stdout.strip() if revision.returncode == 0 else "fixture-no-git-commit"
    if expected_commit and commit != expected_commit:
        raise ValueError(f"checkout commit mismatch: expected {expected_commit}, got {commit}")
    dirty = _git(root, "status", "--porcelain", "--untracked-files=no")
    tracked_dirty = dirty.returncode == 0 and bool(dirty.stdout.strip())
    return CheckoutFacts(
        root=root,
        commit=commit,
        version=str(package.get("version", "")),
        cordis_version=str(cordis_package.get("version", "")),
        tracked_dirty=tracked_dirty,
        paths=_discover_paths(root),
    )


def build_inventory(checkout: Path, *, expected_commit: str | None = None, as_of: str) -> dict[str, Any]:
    facts = inspect_checkout(checkout, expected_commit=expected_commit)
    package_manifests = [path for path in facts.paths if path.startswith("packages/") and path.endswith("/package.json")]
    typescript = [path for path in facts.paths if path.endswith((".ts", ".tsx"))]
    tests = [path for path in facts.paths if "/tests/" in path and path.endswith((".ts", ".tsx", ".py"))]
    evidence_paths = [
        "AGENTS.md",
        "docs/architecture.md",
        "docs/cordis-primer.md",
        "docs/tool-execution-pipeline.md",
        "vendor/README.md",
        "vendor/cordis/src/fiber.ts",
        "packages/core/session/src/index.ts",
        "packages/core/agent-loop/src/invariant.ts",
        "packages/core/tools/src/index.ts",
    ]
    evidence = []
    for relative in evidence_paths:
        path = _safe_file(facts.root, relative)
        if path.is_file():
            evidence.append({"path": relative, "sha256": sha256_file(path)})
    return {
        "schema": INVENTORY_SCHEMA,
        "as_of": as_of,
        "commit": facts.commit,
        "package_version": facts.version,
        "cordis_local_version": facts.cordis_version,
        "tracked_dirty": facts.tracked_dirty,
        "counts": {
            "tracked_allowed_paths": len(facts.paths),
            "package_manifests": len(package_manifests),
            "typescript_files": len(typescript),
            "test_files": len(tests),
        },
        "paths": list(facts.paths),
        "evidence": evidence,
        "limits": [
            "Inventory records allowlisted relative paths and selected hashes, not file contents.",
            "Tracked-dirty state excludes untracked files and does not enumerate filenames.",
            "Inventory does not prove runtime, browser, provider, platform, or production behavior.",
        ],
    }


def load_rules(path: Path) -> list[dict[str, Any]]:
    data = _json_object(path)
    if data.get("schema") != "deepseek-harness.portability-rules.v1":
        raise ValueError("unsupported portability rules schema")
    rules = data.get("subsystems")
    if not isinstance(rules, list) or not rules:
        raise ValueError("portability rules must contain subsystems")
    return [rule for rule in rules if isinstance(rule, dict)]


def synthesize_portability(inventory: dict[str, Any], rules: list[dict[str, Any]]) -> dict[str, Any]:
    if inventory.get("schema") != INVENTORY_SCHEMA:
        raise ValueError("unsupported inventory schema")
    observed = set(inventory.get("paths") or [])
    rows = []
    for rule in rules:
        evidence_paths = [str(item) for item in rule.get("evidence_paths") or []]
        present = [path for path in evidence_paths if path in observed]
        if evidence_paths and len(present) == len(evidence_paths):
            support = "supported"
        elif present:
            support = "partial"
        else:
            support = "no-data"
        rows.append({**rule, "support": support, "observed_evidence_paths": present})
    return {
        "schema": PORTABILITY_SCHEMA,
        "as_of": inventory.get("as_of"),
        "commit": inventory.get("commit"),
        "package_version": inventory.get("package_version"),
        "subsystems": rows,
        "evidence_boundary": "Support reports path presence in the inspected checkout. Portability rank and advice are practitioner synthesis, not upstream guarantees.",
    }


def portability_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# DeepSeek Harness Portability Report",
        "",
        f"Pinned commit: `{report.get('commit', '')}`.",
        "",
        f"Evidence boundary: {report.get('evidence_boundary', '')}",
        "",
        "| Subsystem | Rank | Support | Minimal slice | Recommendation |",
        "|---|---:|---|---|---|",
    ]
    for row in report.get("subsystems") or []:
        lines.append("| {name} | {rank} | {support} | {minimal} | {recommendation} |".format(
            name=str(row.get("name", "")).replace("|", "\\|"),
            rank=row.get("rank", ""),
            support=row.get("support", ""),
            minimal=str(row.get("minimal_slice", "")).replace("|", "\\|"),
            recommendation=str(row.get("recommendation", "")).replace("|", "\\|"),
        ))
    lines.extend(["", "## Evidence Paths", ""])
    for row in report.get("subsystems") or []:
        lines.append(f"### {row.get('name', '')}")
        lines.append("")
        paths = row.get("observed_evidence_paths") or []
        if paths:
            lines.extend(f"- `{path}`" for path in paths)
        else:
            lines.append("- No inspected evidence path was present.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def markdown_report_html(markdown: str) -> str:
    body = []
    in_table = False
    for line in markdown.splitlines():
        if line.startswith("|---"):
            continue
        if line.startswith("| "):
            cells = [html.escape(cell.strip()) for cell in line.strip("|").split("|")]
            tag = "th" if not in_table else "td"
            if not in_table:
                body.append("<table>")
                in_table = True
            body.append("<tr>" + "".join(f"<{tag}>{cell}</{tag}>" for cell in cells) + "</tr>")
            continue
        if in_table:
            body.append("</table>")
            in_table = False
        if line.startswith("# "):
            body.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("### "):
            body.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif line.startswith("- "):
            body.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.strip():
            body.append(f"<p>{html.escape(line)}</p>")
    if in_table:
        body.append("</table>")
    style = "body{font:16px system-ui;max-width:1100px;margin:40px auto;padding:0 20px;color:#202124}table{border-collapse:collapse;width:100%}th,td{border:1px solid #dadce0;padding:8px;text-align:left;vertical-align:top}th{background:#f1f3f4}code{background:#f1f3f4;padding:2px 4px}"
    return "<!doctype html><html><meta charset='utf-8'><title>DeepSeek Harness Portability Report</title><style>" + style + "</style><body>" + "\n".join(body) + "</body></html>\n"
