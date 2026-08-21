## Summary

Describe what changed and why.

## Change type

- [ ] Code or CLI
- [ ] Vault or generated output
- [ ] Research, evidence, or claim ledger
- [ ] Domain adapter or portability rules
- [ ] Community documentation
- [ ] Release or security boundary

## Evidence and generated-content impact

- Source or claim-ledger impact:
- Template and sample-vault synchronization impact:
- Maturity or verification impact:
- Upstream attribution or license impact:

## Verification actually run

List exact commands and results. For behavior or release changes, normally run:

```bash
python tests/test_harness_adapter.py
python tests/test_pipeline.py
```

Checks not run, with reason:

## Release risk

- [ ] No credentials, private client data, local paths, or runtime artifacts were added.
- [ ] Raw-source immutability and manifest coverage are preserved.
- [ ] New domain claims cite dated trustworthy sources.
- [ ] Generated outputs were changed through their owning generator.
- [ ] This change does not claim community or market readiness without the matching release gate.
