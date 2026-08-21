---
name: deepseek-harness-brain
description: >
  Scaffold and operate DeepSeek Harness Brain, a source-cited Obsidian brain for DeepSeek Harness architecture, operations, extension development, security, testing, and debugging.
  Use when the user says "deepseek-harness-brain", "DeepSeek Harness Brain", "create a DeepSeek Harness architecture, operations, extension development, security, testing, and debugging brain",
  "import sources", "synthesize plan", "render report", or wants a persistent
  vault-backed operating system for DeepSeek Harness architecture, operations, extension development, security, testing, and debugging.
argument-hint: "new | ingest | import-checkout | synthesize | portability | portability-html | report | visuals | lint | hash | next"
license: MIT
---

# DeepSeek Harness Brain

Operate the deployed vault first. Treat `CODEX.md`, `wiki/hot.md`, and
`wiki/index.md` as vault-root-relative paths, where the vault root is the
directory passed to `--vault` or opened in Obsidian. In this repo, the template
vault root is `assets/template-brain/` and the demo vault root is
`examples/sample-vault/`.

Secretary: use `agents/deepseek-harness-secretary.md` for grounded answers, claim review,
and vault maintenance. That secretary reads the brain first, cites a vault note
and an official URL, and stays advisory and read-only.

## Commands

```bash
/deepseek-harness-brain new <client-slug> --owner <name>
/deepseek-harness-brain ingest --vault <path> --file <source>
/deepseek-harness-brain import-checkout --checkout <path> --vault <path> --expected-commit <sha> --as-of <date>
/deepseek-harness-brain synthesize --vault <path>
/deepseek-harness-brain portability --inventory <json> --json-out <json> --markdown-out <md>
/deepseek-harness-brain portability-html --markdown <md> --out <html>
/deepseek-harness-brain report --vault <path>
/deepseek-harness-brain visuals --vault <path>
/deepseek-harness-brain lint --vault <path>
/deepseek-harness-brain hash --vault <path> --check <fixture>
/deepseek-harness-brain next --vault <path>
```

Source checkout equivalent:

```bash
deepseek-harness-brain new <client-slug> --owner <name>
deepseek-harness-brain ingest --vault <path> --file <source>
deepseek-harness-brain import-checkout --checkout <path> --vault <path> --expected-commit <sha> --as-of <date>
deepseek-harness-brain synthesize --vault <path>
deepseek-harness-brain report --vault <path> --html-only
```

## Required Operating Rules

1. Read `<vault>/CODEX.md`.
2. Read `<vault>/wiki/hot.md`.
3. Read `<vault>/wiki/index.md`.
4. Preserve `.raw/` as immutable source material.
5. Never store credentials in the vault.
6. Never make domain-specific claims without dated trustworthy sources.
7. Keep `hot`, `index`, `overview`, and `log` current.
8. Record research evidence in `references/source-ledger.json`.
9. Record domain adapter completion in `references/adapter-manifest.json`.

## Script Mapping

- `new` -> `python scripts/scaffold_vault.py`
- `ingest` -> `python scripts/ingest_source.py`
- `import-checkout` -> `python scripts/import_deepseek_harness.py`
- `synthesize` -> `python scripts/synthesize_brain.py`
- `portability` -> `python scripts/synthesize_deepseek_harness.py`
- `portability-html` -> `python scripts/render_portability_report.py`
- `report` -> `python scripts/render_brain_report.py`
- `visuals` -> `python scripts/generate_vault_visuals.py`
- `lint` -> `python scripts/lint_vault.py`
- `hash` -> `python scripts/hash_vault.py`
- `next` -> `python scripts/guide_next_action.py`

## Quality Gates

- No claim that a keyless, static, build, snapshot, browser, or real-API check proves a stronger tier than it actually ran
- No invented package behavior, event semantics, defaults, compatibility promise, vulnerability, benchmark, or release status
- No credentials, tokens, cookies, private settings, or local secret values in brain artifacts
- No instruction to weaken sandbox, approval, host-trust, or credential boundaries merely to make a command pass
- No mutation, publication, deployment, account change, or production action from this advisory brain
- No reliance on archived Agent Notes as current authority when source or current documentation disagrees

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes and `references/release-status.json` records an explicit
human-reviewed market-ready decision. Demo verification is not market readiness.

## Research Refresh

on every DeepSeek Harness release or architecture change; monthly while the project remains in developer preview
