#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.determinism import read_tree_fixture, tree_sha256


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compute or verify a deterministic vault tree hash.")
    parser.add_argument("--vault", required=True)
    parser.add_argument("--check", default="")
    args = parser.parse_args(argv)
    try:
        actual = tree_sha256(Path(args.vault))
        if args.check:
            expected = read_tree_fixture(Path(args.check))
            if actual != expected:
                print(f"ERROR: vault tree hash mismatch: expected {expected}, got {actual}", file=sys.stderr)
                return 1
        print(actual)
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
