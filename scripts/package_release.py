#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".base", ".canvas", ".cjs", ".css", ".csv", ".html", ".js", ".json", ".jsx", ".lock", ".md", ".mjs", ".py", ".sh", ".svg", ".toml", ".ts", ".tsx", ".txt", ".xml", ".yaml", ".yml"}
SKIP_PARTS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".transactions", ".vault-meta", ".venv", "__pycache__", "build", "dist", "venv"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".log"}
FORBIDDEN_ENTRY_NAMES = {".env", ".env.local", ".env.production", ".DS_Store", "Thumbs.db", "workspace.json"}
MAX_SCAN_BYTES = 25 * 1024 * 1024
FORBIDDEN_TEXT_PATTERNS = {
    "local home path": re.compile(rb"/home/(?!\.\.\.)[A-Za-z0-9_.-]+"),
    "private key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai api key": re.compile(rb"sk-[A-Za-z0-9_-]{20,}"),
    "anthropic api key": re.compile(rb"sk-ant-[A-Za-z0-9_-]{20,}"),
    "github token": re.compile(rb"(ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    "aws key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "google api key": re.compile(rb"AIza[0-9A-Za-z_-]{20,}"),
    "bearer literal": re.compile(rb"Bearer\s+[A-Za-z0-9._-]{24,}"),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build verified release ZIP artifacts.")
    parser.add_argument("--version", required=True)
    parser.add_argument("--dist-dir", default="dist")
    parser.add_argument("--release-type", default="scaffold", choices=["scaffold", "demo", "community-ready", "market-ready"])
    args = parser.parse_args(argv)
    version = normalize_version(args.version)
    validate_version_alignment(version)
    dist = (REPO / args.dist_dir).resolve()
    if dist != REPO and not dist.is_relative_to(REPO):
        raise SystemExit(f"ERROR: --dist-dir must resolve inside the repo: {dist}")
    dist.mkdir(parents=True, exist_ok=True)
    gate: dict[str, object] | None = None
    if args.release_type == "community-ready":
        gate = enforce_release_gate("community-ready")
    elif args.release_type == "market-ready":
        gate = enforce_market_ready_gate()
    if gate and git_commit() is None:
        raise SystemExit(f"ERROR: {args.release_type} release requires a Git checkout with a resolved commit")
    validate_distribution_license()
    scan_source_tree()
    artifacts = [
        build_zip(dist / f"deepseek-harness-brain-template-v{version}.zip", REPO / "assets" / "template-brain", "deepseek-harness-brain-template"),
        build_zip(dist / f"deepseek-harness-brain-sample-vault-v{version}.zip", REPO / "examples" / "sample-vault", "deepseek-harness-brain-sample-vault"),
        build_source_zip(dist / f"deepseek-harness-brain-source-v{version}.zip", version),
    ]
    for artifact in artifacts:
        validate_zip(artifact["path"])
    manifest = {
        "schema": "deepseek-harness-brain.release-manifest.v2",
        "product": "deepseek-harness-brain",
        "version": version,
        "release_type": args.release_type,
        "generated_at": deterministic_release_datetime().isoformat(),
        "git_commit": git_commit(),
        "artifacts": [{"file": a["path"].name, "sha256": sha256_file(a["path"]), "bytes": a["path"].stat().st_size, "entries": a["entries"]} for a in artifacts],
        "checks": [
            *([f"{args.release_type} audit passed"] if gate else []),
            "repo source scan passed",
            "zip entry scan passed",
            "zip content secret scan passed",
            "zip content local-path scan passed",
        ],
    }
    if gate:
        manifest["gate"] = gate
    manifest_path = dist / "RELEASE_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sums = dist / "SHA256SUMS"
    write_sha256s(sums, [*(a["path"] for a in artifacts), manifest_path])
    validate_sha256s(sums)
    print(f"Release package built in {dist}")
    return 0


def enforce_release_gate(required_status: str) -> dict[str, object]:
    audit = REPO / "scripts" / "audit_brain.py"
    if not audit.exists():
        raise SystemExit(f"ERROR: {required_status} release blocked: missing scripts/audit_brain.py")
    proc = subprocess.run(
        [sys.executable, str(audit), "--require", required_status, "--json"],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode:
        detail = "\n".join(part for part in [proc.stdout.strip(), proc.stderr.strip()] if part)
        raise SystemExit(f"ERROR: {required_status} release blocked by audit:\n" + detail)
    try:
        result = json.loads(proc.stdout)
    except ValueError as exc:
        raise SystemExit(f"ERROR: {required_status} release blocked: audit returned invalid JSON: {exc}") from exc
    allowed = {"community-ready", "market-ready"} if required_status == "community-ready" else {"market-ready"}
    if result.get("status") not in allowed or result.get("critical_failures"):
        raise SystemExit(f"ERROR: {required_status} release blocked: audit result is inconsistent")
    release_status = REPO / "references" / "release-status.json"
    release = json.loads(release_status.read_text(encoding="utf-8"))
    return {
        "required_maturity": required_status,
        "observed_maturity": result["status"],
        "score": result["score"],
        "critical_failures": result["critical_failures"],
        "release_status_schema": release.get("schema"),
        "release_status_as_of": release.get("as_of"),
        "release_status_sha256": sha256_file(release_status),
    }


def enforce_market_ready_gate() -> dict[str, object]:
    return enforce_release_gate("market-ready")


def normalize_version(value: str) -> str:
    version = value.strip().removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit("ERROR: --version must look like 0.1.0")
    return version


def validate_version_alignment(version: str) -> None:
    surfaces: dict[str, str] = {}
    patterns = {
        "pyproject.toml": r'(?m)^version = "([^"]+)"$',
        "deepseek_harness_brain/__init__.py": r'(?m)^__version__ = "([^"]+)"$',
        "CITATION.cff": r"(?m)^version: ([^\s]+)$",
    }
    for rel, pattern in patterns.items():
        match = re.search(pattern, (REPO / rel).read_text(encoding="utf-8"))
        surfaces[rel] = match.group(1) if match else ""
    plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    marketplace = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    release = json.loads((REPO / "references" / "release-status.json").read_text(encoding="utf-8"))
    surfaces[".claude-plugin/plugin.json"] = plugin.get("version", "")
    surfaces[".claude-plugin/marketplace.json metadata"] = marketplace.get("metadata", {}).get("version", "")
    surfaces[".claude-plugin/marketplace.json plugin"] = marketplace.get("plugins", [{}])[0].get("version", "")
    surfaces["references/release-status.json"] = release.get("release_version", "")
    mismatched = [f"{name}={actual or '<missing>'}" for name, actual in surfaces.items() if actual != version]
    if f"## {version} " not in (REPO / "CHANGELOG.md").read_text(encoding="utf-8"):
        mismatched.append("CHANGELOG.md=<missing release heading>")
    if mismatched:
        raise SystemExit("ERROR: release version does not match metadata: " + ", ".join(mismatched))


def deterministic_release_datetime() -> datetime:
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "").strip()
    if epoch:
        try:
            return datetime.fromtimestamp(int(epoch), tz=timezone.utc).replace(microsecond=0)
        except (OverflowError, ValueError) as exc:
            raise SystemExit("ERROR: SOURCE_DATE_EPOCH must be a valid Unix timestamp") from exc
    release = json.loads((REPO / "references" / "release-status.json").read_text(encoding="utf-8"))
    try:
        return datetime.fromisoformat(str(release["as_of"]) + "T00:00:00+00:00")
    except (KeyError, ValueError) as exc:
        raise SystemExit("ERROR: release-status.json requires a valid as_of date") from exc


def write_zip_member(zf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    timestamp = deterministic_release_datetime()
    if timestamp.year < 1980:
        timestamp = datetime(1980, 1, 1, tzinfo=timezone.utc)
    info = zipfile.ZipInfo(arcname, date_time=timestamp.timetuple()[:6])
    info.create_system = 3
    mode = 0o755 if path.stat().st_mode & stat.S_IXUSR else 0o644
    info.external_attr = (stat.S_IFREG | mode) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def validate_distribution_license() -> None:
    path = REPO / "LICENSE"
    if not path.is_file():
        raise SystemExit("ERROR: release blocked: LICENSE is missing")
    license_text = path.read_text(encoding="utf-8")
    placeholders = ("Replace this file", "all rights are reserved")
    if "MIT License" not in license_text or any(marker in license_text for marker in placeholders):
        raise SystemExit("ERROR: release blocked: LICENSE is incomplete or still a placeholder")


def should_skip(path: Path) -> bool:
    if set(path.parts) & SKIP_PARTS:
        return True
    if any(part.endswith(".egg-info") for part in path.parts):
        return True
    return path.suffix in SKIP_SUFFIXES


def reject_forbidden_entry(path: Path) -> None:
    if path.name in FORBIDDEN_ENTRY_NAMES:
        raise SystemExit(f"ERROR: forbidden release entry: {path.as_posix()}")
    if path.is_absolute() or ".." in path.parts:
        raise SystemExit(f"ERROR: unsafe release entry: {path.as_posix()}")


def iter_tree(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if should_skip(rel):
            continue
        reject_forbidden_entry(rel)
        if path.is_symlink():
            raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
        if path.is_file():
            files.append(path)
    return sorted(files)


def source_files() -> list[Path]:
    if (REPO / ".git").exists():
        reject_dirty_tracked_files()
        reject_untracked_files()
        proc = subprocess.run(["git", "ls-files", "-z", "--cached"], cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        files = []
        for raw in proc.stdout.split(b"\0"):
            if raw:
                rel = Path(raw.decode("utf-8", "replace"))
                if should_skip(rel):
                    continue
                reject_forbidden_entry(rel)
                path = REPO / rel
                if path.is_symlink():
                    raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
                if path.is_file():
                    files.append(path)
        return sorted(files)
    return iter_tree(REPO)


def reject_dirty_tracked_files() -> None:
    dirty: set[str] = set()
    for args in (["git", "diff", "--name-only", "-z"], ["git", "diff", "--name-only", "-z", "--cached"]):
        proc = subprocess.run(args, cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        dirty.update(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    blocked = sorted(path for path in dirty if not should_skip(Path(path)))
    if blocked:
        raise SystemExit("ERROR: dirty tracked files would make release non-reproducible: " + ", ".join(blocked[:10]))


def reject_untracked_files() -> None:
    proc = subprocess.run(["git", "ls-files", "-z", "--others", "--exclude-standard"], cwd=REPO, capture_output=True, check=False)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.decode("utf-8", "replace"))
    untracked = sorted(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    allowed = [p for p in untracked if not should_skip(Path(p))]
    if allowed:
        raise SystemExit("ERROR: untracked files would make release non-reproducible: " + ", ".join(allowed[:10]))


def scan_source_tree() -> None:
    for path in source_files():
        rel = path.relative_to(REPO)
        if not should_skip(rel):
            scan_file(path, rel.as_posix())


def build_zip(out: Path, source: Path, root_name: str) -> dict[str, object]:
    entries = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in iter_tree(source):
            write_zip_member(zf, path, (Path(root_name) / path.relative_to(source)).as_posix())
            entries += 1
        for relative in (Path("LICENSE"), Path("THIRD_PARTY_NOTICES.md"), Path("licenses/DEEPSEEK-HARNESS-MIT.txt"), Path("references/public-capture-allowlist.json")):
            write_zip_member(zf, REPO / relative, (Path(root_name) / relative).as_posix())
            entries += 1
    return {"path": out, "entries": entries}


def build_source_zip(out: Path, version: str) -> dict[str, object]:
    entries = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in source_files():
            rel = path.relative_to(REPO)
            if not should_skip(rel):
                write_zip_member(zf, path, (Path(f"deepseek-harness-brain-v{version}") / rel).as_posix())
                entries += 1
    return {"path": out, "entries": entries}


def validate_zip(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names:
            raise SystemExit(f"ERROR: empty artifact: {path.name}")
        for name in names:
            rel = Path(name)
            for part in rel.parts:
                reject_forbidden_entry(Path(part))
            if should_skip(rel) or any(part in SKIP_PARTS for part in rel.parts):
                raise SystemExit(f"ERROR: forbidden zip entry in {path.name}: {name}")
            mode = zf.getinfo(name).external_attr >> 16
            if stat.S_ISLNK(mode):
                raise SystemExit(f"ERROR: symlink entry in {path.name}: {name}")
            scan_bytes(zf.read(name), f"{path.name}:{name}", rel.suffix)


def scan_file(path: Path, label: str) -> None:
    size = path.stat().st_size
    if size > MAX_SCAN_BYTES:
        raise SystemExit(f"ERROR: file too large for release scan: {label}")
    scan_bytes(path.read_bytes(), label, path.suffix)


def scan_bytes(data: bytes, label: str, suffix: str) -> None:
    if suffix and suffix not in TEXT_SUFFIXES and b"\0" in data[:8192]:
        return
    for name, pattern in FORBIDDEN_TEXT_PATTERNS.items():
        if pattern.search(data):
            raise SystemExit(f"ERROR: {name} found in {label}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sha256s(path: Path, artifacts: list[Path]) -> None:
    path.write_text("\n".join(f"{sha256_file(a)}  {a.name}" for a in artifacts) + "\n", encoding="utf-8")


def validate_sha256s(path: Path) -> None:
    for line in path.read_text(encoding="utf-8").splitlines():
        expected, filename = line.split("  ", 1)
        actual = sha256_file(path.parent / filename)
        if expected != actual:
            raise SystemExit(f"ERROR: checksum mismatch for {filename}")


def git_commit() -> str | None:
    if not (REPO / ".git").exists():
        return None
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else None


if __name__ == "__main__":
    raise SystemExit(main())
