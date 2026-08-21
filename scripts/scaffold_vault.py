#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.determinism import parse_as_of

TEMPLATE = REPO / "assets" / "template-brain"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold a client vault from the template brain.")
    parser.add_argument("--client", required=True)
    parser.add_argument("--client-name", default="")
    parser.add_argument("--owner", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--as-of", default="")
    args = parser.parse_args(argv)
    as_of = parse_as_of(args.as_of).isoformat()
    slug = safe_slug(args.client)
    out_dir = Path(args.out_dir).expanduser().resolve()
    vault = out_dir / slug
    if vault.exists() and any(vault.iterdir()) and not args.force:
        print(f"ERROR: vault exists and is not empty: {vault}", file=sys.stderr)
        return 2
    if not TEMPLATE.exists():
        print(f"ERROR: template missing: {TEMPLATE}", file=sys.stderr)
        return 2
    if vault.exists():
        shutil.rmtree(vault)
    copy_template(TEMPLATE, vault, {
        "{{date}}": as_of,
        "{{client_slug}}": slug,
        "{{client_name}}": args.client_name or slug,
        "{{owner}}": args.owner,
    })
    for raw_source in (vault / ".raw" / "sources").glob("*"):
        if raw_source.is_file():
            raw_source.chmod(0o600)
    copy_reference_pack(REPO / "references", vault / "references")
    manifest = vault / ".raw" / ".manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest_data = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else {"sources": []}
    if not isinstance(manifest_data, dict):
        raise SystemExit("ERROR: template raw manifest must be an object")
    sources = manifest_data.get("sources")
    if not isinstance(sources, list):
        raise SystemExit("ERROR: template raw manifest sources must be a list")
    manifest_data["scaffold_history"] = [{
            "client": slug,
            "client_name": args.client_name or slug,
            "owner": args.owner,
            "created": as_of,
        }]
    manifest.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")
    manifest.chmod(0o600)
    print(vault)
    return 0


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug or slug in {".", ".."}:
        raise SystemExit("ERROR: invalid client slug")
    return slug


def copy_template(src: Path, dest: Path, replacements: dict[str, str]) -> None:
    for path in sorted(src.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        if ".vault-meta" in rel.parts:
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            target.write_bytes(data)
            continue
        for old, new in replacements.items():
            text = text.replace(old, new)
        target.write_text(text, encoding="utf-8")


def copy_reference_pack(src: Path, dest: Path) -> None:
    """Copy the bounded, non-secret evidence pack into a deployed vault."""
    allowed_files = {
        "adapter-manifest.json",
        "claim-ledger.md",
        "portability-rules.json",
        "release-status.json",
        "source-ledger.json",
        "verification-ledger.json",
    }
    for path in sorted(src.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(src)
        if relative.parts[0] not in {"canon", "schemas"} and relative.as_posix() not in allowed_files:
            continue
        target = dest / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


if __name__ == "__main__":
    raise SystemExit(main())
