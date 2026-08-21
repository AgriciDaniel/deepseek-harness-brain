# Contributing

Thank you for improving DeepSeek Harness Brain. Small, source-cited changes are
easier to review and safer to merge.

## Before you begin

- Use Python 3.11 or newer.
- Read `README.md`, `docs/PRODUCT_BOUNDARIES.md`, and the relevant vault's `CODEX.md`.
- Search existing issues before opening a new one.
- Use `SECURITY.md` instead of an issue for sensitive findings.
- Do not commit credentials, private client data, local paths, copied proprietary
  material, or generated archives.

## Local setup

```bash
python -m pip install -e .
deepseek-harness-brain --help
```

## Evidence rules

- Domain claims need a dated trustworthy source.
- Prefer official repositories, documentation, standards, and primary research.
- Preserve `.raw/` captures as immutable evidence.
- Record new evidence in `references/source-ledger.json` and claim changes in
  `references/claim-ledger.md`.
- Mark practitioner recommendations as recommendations, not repository facts.
- Try to refute important claims before strengthening them.
- Never promote maturity through prose alone.

The committed `.raw/` files are a reviewed allowlist of public upstream material.
Never add private, credential-bearing, account-derived, or client-specific raw
captures to this repository.

## Making a change

1. Create a focused branch.
2. Change only the relevant code, note, ledger, fixture, or generated artifact.
3. If a generator owns an output, change the generator first and regenerate it.
4. Keep the template vault and sample vault synchronized when their shared
   structure changes.
5. Add or update tests for behavior changes.
6. Report the exact checks you ran and any checks you skipped.

## Verification

Run the focused check first, then the complete local pipeline when the change can
affect packaging, vault structure, imports, synthesis, or release status.

```bash
python tests/test_harness_adapter.py
python tests/test_pipeline.py
```

For documentation-only changes, at minimum run the two vault linters:

```bash
python scripts/lint_vault.py --vault assets/template-brain --template
python scripts/lint_vault.py --vault examples/sample-vault
```

## Pull requests

Explain what changed, why it is needed, the evidence affected, and the checks
actually run. Call out changes to maturity, security boundaries, licensing,
upstream attribution, generated content, or compatibility.

By contributing, you agree that your contribution may be distributed under the
repository's MIT license. Upstream material must retain its original attribution
and license.
