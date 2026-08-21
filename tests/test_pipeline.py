#!/usr/bin/env python3
from __future__ import annotations

import json
import importlib.util
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run([PY, *args], cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def run_cmd(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(args, cwd=REPO, text=True, capture_output=True, env={**os.environ, **(env or {})}, check=False)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    return proc


def main() -> int:
    package_spec = importlib.util.spec_from_file_location("deepseek_harness_package_release", REPO / "scripts" / "package_release.py")
    if package_spec is None or package_spec.loader is None:
        raise AssertionError("unable to load repository package_release.py")
    package_module = importlib.util.module_from_spec(package_spec)
    package_spec.loader.exec_module(package_module)
    scan_bytes = package_module.scan_bytes

    for suffix in (".mjs", ".svg"):
        try:
            scan_bytes(b"github_pat_" + b"A" * 30, f"scanner-fixture{suffix}", suffix)
        except SystemExit:
            pass
        else:
            raise AssertionError(f"release scanner ignored a credential pattern in {suffix}")
    run(["-m", "compileall", "scripts", "deepseek_harness_brain", "tests"])
    run(["tests/test_harness_adapter.py"])
    run(["scripts/lint_vault.py", "--vault", "assets/template-brain", "--template"])
    with tempfile.TemporaryDirectory(prefix="deepseek-harness-brain-test-") as tmp:
        out_dir = Path(tmp) / "vaults"
        run(["scripts/scaffold_vault.py", "--client", "acme", "--client-name", "Acme Co", "--owner", "Test Owner", "--out-dir", str(out_dir), "--as-of", "2026-08-21"])
        vault = out_dir / "acme"
        import_args = ["scripts/import_deepseek_harness.py", "--checkout", "tests/fixtures/harness-checkout", "--vault", str(vault), "--as-of", "2026-08-21"]
        run(import_args)
        run(import_args)
        raw_manifest = json.loads((vault / ".raw" / ".manifest.json").read_text(encoding="utf-8"))
        inventories = [item for item in raw_manifest["sources"] if "deepseek-harness-inventory" in item.get("path", "")]
        assert len(inventories) == 1
        run(["scripts/ingest_source.py", "--vault", str(vault), "--file", "tests/fixtures/sample-source.md", "--as-of", "2026-08-21"])
        run(["scripts/synthesize_brain.py", "--vault", str(vault), "--as-of", "2026-08-21"])
        run(["scripts/generate_vault_visuals.py", "--vault", str(vault)])
        run(["scripts/render_brain_report.py", "--vault", str(vault), "--html-only"])
        run(["scripts/lint_vault.py", "--vault", str(vault)])
        assert (vault / "weekly-report.html").exists()
    run(["scripts/build_demo_vault.py"])
    run(["scripts/hash_vault.py", "--vault", "examples/sample-vault", "--check", "tests/fixtures/sample-vault.sha256"])
    audit = run(["scripts/audit_brain.py", "--json", "--report-only"])
    audit_result = json.loads(audit.stdout)
    market_ready = audit_result.get("market_ready") is True or audit_result.get("status") == "market-ready"
    gated = subprocess.run([PY, "scripts/package_release.py", "--version", "0.2.0", "--release-type", "market-ready"], cwd=REPO, text=True, capture_output=True, check=False)
    if market_ready:
        if gated.returncode:
            print(gated.stdout)
            print(gated.stderr, file=sys.stderr)
        assert gated.returncode == 0
        manifest = REPO / "dist" / "RELEASE_MANIFEST.json"
        assert manifest.exists()
        assert json.loads(manifest.read_text(encoding="utf-8")).get("release_type") == "market-ready"
    else:
        assert gated.returncode != 0
        assert "market-ready release blocked" in gated.stderr
    run(["scripts/package_release.py", "--version", "0.2.0", "--release-type", "demo"])
    assert (REPO / "dist" / "RELEASE_MANIFEST.json").exists()
    for artifact_name in (
        "deepseek-harness-brain-template-v0.2.0.zip",
        "deepseek-harness-brain-sample-vault-v0.2.0.zip",
    ):
        with zipfile.ZipFile(REPO / "dist" / artifact_name) as archive:
            names = archive.namelist()
            assert any(name.endswith("/LICENSE") for name in names)
            assert any(name.endswith("/THIRD_PARTY_NOTICES.md") for name in names)
            assert any(name.endswith("/licenses/DEEPSEEK-HARNESS-MIT.txt") for name in names)
    with tempfile.TemporaryDirectory(prefix="deepseek-harness-brain-install-") as tmp:
        env = {"DEEPSEEK_HARNESS_BRAIN_INSTALL_HOME": tmp}
        run_cmd(["bash", "install.sh", "--target", "all"], env=env)
        assert (Path(tmp) / ".codex" / "skills" / "deepseek-harness-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".openclaw" / "skills" / "deepseek-harness-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".agent-skills" / "deepseek-harness-brain" / "SKILL.md").exists()
        assert (Path(tmp) / ".gemini" / "deepseek-harness-brain" / "GEMINI.md").exists()
        assert "deepseek-harness-brain-install:start" in (Path(tmp) / ".gemini" / "GEMINI.md").read_text(encoding="utf-8")
        custom_root = Path(tmp) / "custom-skills"
        run_cmd(["bash", "install.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert (custom_root / "deepseek-harness-brain" / "SKILL.md").exists()
        run_cmd(["bash", "uninstall.sh", "--target", "all"], env=env)
        assert not (Path(tmp) / ".codex" / "skills" / "deepseek-harness-brain").exists()
        assert not (Path(tmp) / ".gemini" / "deepseek-harness-brain").exists()
        assert not (Path(tmp) / ".gemini" / "GEMINI.md").exists()
        run_cmd(["bash", "uninstall.sh", "--target", "custom", "--path", str(custom_root)], env=env)
        assert not (custom_root / "deepseek-harness-brain").exists()
    print("Pipeline tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
