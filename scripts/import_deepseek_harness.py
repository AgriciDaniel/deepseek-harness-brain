#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.determinism import parse_as_of
from deepseek_harness_brain.harness_adapter import build_inventory


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect an allowlisted DeepSeek Harness checkout into deterministic JSON.")
    parser.add_argument("--checkout", required=True)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--vault", help="Write a content-addressed raw inventory and manifest entry into this vault.")
    destination.add_argument("--out", help="Write the inventory to an explicit path for diagnostics or pipelines.")
    parser.add_argument("--expected-commit", default="")
    parser.add_argument("--as-of", default="")
    args = parser.parse_args(argv)
    try:
        as_of = parse_as_of(args.as_of).isoformat()
        inventory = build_inventory(
            Path(args.checkout),
            expected_commit=args.expected_commit or None,
            as_of=as_of,
        )
        payload = json.dumps(inventory, indent=2, sort_keys=True) + "\n"
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        if args.vault:
            vault = Path(args.vault).expanduser().resolve()
            if not (vault / "CODEX.md").is_file():
                raise ValueError(f"not a brain vault: {vault}")
            safe_commit = "".join(char for char in inventory["commit"] if char.isalnum())[:12] or "unknown"
            output = vault / ".raw" / "sources" / f"deepseek-harness-inventory-{safe_commit}-{digest[:12]}.json"
        else:
            output = Path(args.out).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists() and output.read_text(encoding="utf-8") != payload:
            raise ValueError(f"refusing to overwrite different bytes: {output}")
        if not output.exists():
            output.write_text(payload, encoding="utf-8")
        output.chmod(0o600)
        if args.vault:
            update_manifest(vault, output.relative_to(vault).as_posix(), digest, as_of)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(output)
    return 0


def update_manifest(vault: Path, relative: str, digest: str, as_of: str) -> None:
    path = vault / ".raw" / ".manifest.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"sources": []}
    if not isinstance(data, dict) or not isinstance(data.get("sources"), list):
        raise ValueError(f"invalid raw manifest: {path}")
    entries = data["sources"]
    existing = next((item for item in entries if isinstance(item, dict) and item.get("path") == relative), None)
    if existing:
        if existing.get("sha256") != digest:
            raise ValueError(f"manifest records different bytes: {relative}")
        return
    entries.append({"path": relative, "sha256": digest, "retrieved": as_of, "source_type": "official-checkout-inventory"})
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    path.chmod(0o600)


if __name__ == "__main__":
    raise SystemExit(main())
