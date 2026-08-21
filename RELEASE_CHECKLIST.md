# Release Checklist

## Product

- [ ] README states buyer, promise, outputs, boundaries, and quick start.
- [ ] `SKILL.md` maps commands accurately.
- [ ] License and distribution stance is explicit.
- [ ] Third-party notices are current.

## Research

- [ ] Maturity is documented and not overstated.
- [ ] `references/current-requirements.md` has dated official/primary sources.
- [ ] `references/source-ledger.json` lists dated official/primary sources,
      refresh dates, source types, and supported claims.
- [ ] `references/source-map.md` explains import strategy and source schemas.
- [ ] `references/safety-gates.md` lists refusal rules and failure paths.
- [ ] Stale source claims were browsed and refreshed before release.

## Vault

- [ ] Template vault opens in Obsidian.
- [ ] Hot/Index/Wiki notes and hubs are connected.
- [ ] Raw sources stay immutable under `.raw/`.
- [ ] Deliverables cite source notes or raw-file hashes.
- [ ] `PUBLISHING_NOTICE.md` has been reviewed before public publish or ZIP release.

## Verification

- [ ] `python -m compileall scripts deepseek_harness_brain tests`
- [ ] `python tests/test_pipeline.py`
- [ ] `python scripts/build_demo_vault.py`
- [ ] `python scripts/package_release.py --version 0.2.0 --release-type community-ready`
- [ ] No secrets, private client data, or local absolute paths in artifacts.
- [ ] Community release is blocked unless the community-ready audit passes.
- [ ] Market-ready release remains blocked without the separate runtime evidence and human decision.
- [ ] `references/adapter-manifest.json` names real schemas, importer paths,
      synthesis modules, report renderers, fixtures, and tests before
      domain-adapted or market-ready release.

## Community-ready review

- [ ] All focused tests and the complete pipeline passed on the exact release commit.
- [ ] License, third-party notices, raw-capture rights, and trademark wording were reviewed.
- [ ] Source and final archives passed secret, local-path, unsafe-entry, and symlink scans.
- [ ] The community manifest records the observed maturity and release-status digest.
- [ ] Actions permissions, required CI, branch protection, and CODEOWNERS were reviewed.
- [ ] Security policy, private reporting plan, issue forms, and support route were reviewed.
- [ ] `references/release-status.json` records evidence limits without claiming market readiness.
- [ ] Public visibility, tagging, and GitHub release publication remain a separate owner decision.

## Market-ready review

- [ ] Community-ready passed.
- [ ] Browser and live-provider evidence passed.
- [ ] Native and declared cross-platform evidence passed.
- [ ] Comprehensive security review and complete release matrix passed.
- [ ] Production-scale and long-running durability evidence passed.
- [ ] An explicit dated human market-ready decision is recorded.
- [ ] `python scripts/audit_brain.py --require market-ready --json`
