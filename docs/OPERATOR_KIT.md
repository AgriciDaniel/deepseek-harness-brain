# DeepSeek Harness Brain Operator Kit

## Five-Minute Path

```bash
python -m pip install -e .
deepseek-harness-brain demo
deepseek-harness-brain lint --vault examples/sample-vault
deepseek-harness-brain report --vault examples/sample-vault --html-only
```

Open `examples/sample-vault/` in Obsidian and read:

1. `CODEX.md`
2. `wiki/hot.md`
3. `wiki/index.md`
4. `wiki/meta/dashboard.md`

## Client Vault

```bash
deepseek-harness-brain new acme --client-name "Acme Co" --owner "Daniel Agrici" --out-dir ~/deepseek-harness-brain-vaults
deepseek-harness-brain ingest --vault ~/deepseek-harness-brain-vaults/acme --file tests/fixtures/sample-source.md
deepseek-harness-brain synthesize --vault ~/deepseek-harness-brain-vaults/acme
deepseek-harness-brain report --vault ~/deepseek-harness-brain-vaults/acme --html-only
```

## Research Rule

Version 0.2.0 is community-ready and domain-adapted against the pinned upstream
commit. Refresh current official or primary sources before extending its claims
or preparing another release. If evidence is stale, lower confidence instead of
carrying the current status forward automatically.

Research evidence must be written into `references/source-ledger.json` with
source URL, source type, retrieved date, refresh due date, confidence, and claim
coverage. Markdown research notes alone do not satisfy market-ready release.

## Adapter Rule

Domain-adapted status requires `references/adapter-manifest.json` to name real
schemas, importer paths, synthesis modules, report renderers, fixtures, and
tests. The current adapter passes its focused tests. Browser, live-provider,
native, cross-platform, comprehensive security-audit, and production-scale
evidence remain open, so the product is not market-ready.
