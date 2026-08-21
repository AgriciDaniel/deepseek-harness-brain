#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.harness_adapter import load_rules, portability_markdown, synthesize_portability


def load_object(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Synthesize a DeepSeek Harness portability report from an inventory.")
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--rules", default="references/portability-rules.json")
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--markdown-out", required=True)
    args = parser.parse_args(argv)
    try:
        inventory = load_object(Path(args.inventory).expanduser().resolve())
        rules = load_rules(Path(args.rules).expanduser().resolve())
        report = synthesize_portability(inventory, rules)
        json_out = Path(args.json_out).expanduser().resolve()
        markdown_out = Path(args.markdown_out).expanduser().resolve()
        json_out.parent.mkdir(parents=True, exist_ok=True)
        markdown_out.parent.mkdir(parents=True, exist_ok=True)
        json_out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        markdown_out.write_text(portability_markdown(report), encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(markdown_out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
