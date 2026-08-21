#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.harness_adapter import markdown_report_html


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a synthesized DeepSeek Harness portability report as HTML.")
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        markdown = Path(args.markdown).expanduser().resolve().read_text(encoding="utf-8")
        output = Path(args.out).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown_report_html(markdown), encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
