from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from deepseek_harness_brain.harness_adapter import (
    INVENTORY_SCHEMA,
    build_inventory,
    markdown_report_html,
    portability_markdown,
    synthesize_portability,
)
from deepseek_harness_brain.determinism import parse_as_of


FIXTURE = ROOT / "tests" / "fixtures" / "harness-checkout"


def copied_fixture(parent: Path) -> Path:
    checkout = parent / "checkout"
    shutil.copytree(FIXTURE, checkout)
    return checkout


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="dsh-brain-adapter-") as value:
        temp = Path(value)
        checkout = copied_fixture(temp)
        os.environ.pop("DEEPSEEK_API_KEY", None)
        first = build_inventory(checkout, as_of="2026-08-21")
        second = build_inventory(checkout, as_of="2026-08-21")
        assert first == second
        assert first["schema"] == INVENTORY_SCHEMA
        assert first["package_version"] == "0.0.0-fixture"
        assert first["cordis_local_version"] == "0.0.0-fixture"
        assert first["counts"]["package_manifests"] == 1
        encoded = json.dumps(first, sort_keys=True)
        assert str(checkout) not in encoded
        assert "DEEPSEEK_API_KEY" not in encoded
        os.environ["SOURCE_DATE_EPOCH"] = "1787270400"
        assert parse_as_of("") == date(2026, 8, 21)
        os.environ.pop("SOURCE_DATE_EPOCH", None)

        try:
            build_inventory(checkout, expected_commit="not-the-fixture", as_of="2026-08-21")
        except ValueError as exc:
            assert "commit mismatch" in str(exc)
        else:
            raise AssertionError("expected commit mismatch")

        package_path = checkout / "package.json"
        original_package = package_path.read_text(encoding="utf-8")
        package_path.write_text('{"name":"wrong","version":"0"}\n', encoding="utf-8")
        try:
            build_inventory(checkout, as_of="2026-08-21")
        except ValueError as exc:
            assert "root package name" in str(exc)
        else:
            raise AssertionError("expected wrong package identity")
        package_path.write_text("{ malformed\n", encoding="utf-8")
        try:
            build_inventory(checkout, as_of="2026-08-21")
        except ValueError as exc:
            assert "invalid JSON" in str(exc)
        else:
            raise AssertionError("expected malformed package failure")
        package_path.write_text(original_package, encoding="utf-8")

        escape = checkout / "docs" / "escape.md"
        escape.symlink_to(Path(value).parent / "outside.md")
        try:
            build_inventory(checkout, as_of="2026-08-21")
        except ValueError as exc:
            assert "symlinked evidence path" in str(exc)
        else:
            raise AssertionError("expected symlink rejection")
        escape.unlink()

        rules = [
            {
                "id": "supported",
                "name": "Supported",
                "rank": 5,
                "confidence": "evidence-based",
                "minimal_slice": "one",
                "recommendation": "port",
                "evidence_paths": ["packages/core/session/src/index.ts"],
            },
            {
                "id": "partial",
                "name": "Partial",
                "rank": 3,
                "confidence": "practitioner",
                "minimal_slice": "two",
                "recommendation": "study",
                "evidence_paths": ["packages/core/session/src/index.ts", "packages/core/tools/src/index.ts"],
            },
            {
                "id": "no-data",
                "name": "No Data",
                "rank": 1,
                "confidence": "contested",
                "minimal_slice": "three",
                "recommendation": "defer",
                "evidence_paths": ["packages/web/missing.ts"],
            },
        ]
        report = synthesize_portability(first, rules)
        assert [row["support"] for row in report["subsystems"]] == ["supported", "partial", "no-data"]
        assert [row["id"] for row in report["subsystems"]] == ["supported", "partial", "no-data"]
        markdown = portability_markdown(report)
        assert "Pinned commit:" in markdown
        assert "packages/core/session/src/index.ts" in markdown
        rendered = markdown_report_html(markdown)
        assert "DeepSeek Harness Portability Report" in rendered
        assert str(checkout) not in rendered
    print("test_harness_adapter.py: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
