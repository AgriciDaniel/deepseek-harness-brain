#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from deepseek_harness_brain.determinism import read_tree_fixture, tree_sha256

PY = sys.executable


def run(args: list[str]) -> None:
    subprocess.run([PY, *args], cwd=REPO, check=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate the deterministic sample vault.")
    parser.add_argument("--as-of", default="2026-08-21")
    args = parser.parse_args(argv)
    demo_parent = REPO / "examples"
    demo = demo_parent / "sample-vault"
    if demo.exists():
        shutil.rmtree(demo)
    run(["scripts/scaffold_vault.py", "--client", "sample-vault", "--client-name", "Sample Client", "--owner", "Daniel Agrici", "--out-dir", str(demo_parent), "--as-of", args.as_of])
    run(["scripts/ingest_source.py", "--vault", str(demo), "--file", "tests/fixtures/sample-source.md", "--source-type", "fixture", "--as-of", args.as_of])
    run(["scripts/synthesize_brain.py", "--vault", str(demo), "--as-of", args.as_of])
    run(["scripts/generate_vault_visuals.py", "--vault", str(demo)])
    run(["scripts/render_brain_report.py", "--vault", str(demo), "--html-only"])
    run(["scripts/lint_vault.py", "--vault", str(demo)])
    fixture = REPO / "tests" / "fixtures" / "sample-vault.sha256"
    if fixture.exists():
        expected = read_tree_fixture(fixture)
        actual = tree_sha256(demo)
        if actual != expected:
            print(f"ERROR: sample vault hash mismatch: expected {expected}, got {actual}", file=sys.stderr)
            return 1
    print(demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
