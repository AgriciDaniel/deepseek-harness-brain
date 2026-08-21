---
type: "experiment"
title: "Keyless Architecture Verification Results"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/experiment", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Testing evidence tiers]]", "[[Portability Matrix]]", "[[Cordis Fork Delta]]", "[[wiki/experiments/_index|Experiments Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"]
---

# Keyless Architecture Verification Results

Executed on Linux x64, Node 24.16.0, Vitest 4.1.8, commit `b150a551`, on 2026-08-21.

| Probe | Result | Exact scope |
|---|---|---|
| Real Loader composition | PASS | 1 file, 1 test, e2e config, deterministic headless tool round trip and persisted session |
| Request reconstruction | PASS | 2 files, 30 tests |
| Tool registration disposer | PASS | 1 selected test, 135 skipped by name filter |
| Pre-execute denial | PASS | 1 selected test, 135 skipped by name filter |

`pnpm exec vitest` did not run these tests because its dependency check attempted an install and the repository refused to replace the user-owned global Git hooks path. The guard was not bypassed. The installed local Vitest entrypoint ran the focused tests. The first Loader attempt used the default config and found no e2e test files; the passing rerun used `vitest.e2e.config.ts`.

These results do not prove a live DeepSeek provider, browser interaction, native packaging, another platform, hostile-input security, or production durability. Exact commands and proof boundaries live in `references/verification-ledger.json`.

Related: [[Testing evidence tiers]] | [[Action Roadmap]]
