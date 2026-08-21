---
type: "flow"
title: "Installation and Operations"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/flow", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[DeepSeek Harness Review Verdict]]", "[[Testing evidence tiers]]", "[[Keyless Architecture Verification Results]]", "[[Action Roadmap]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/development.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"]
---

# Installation and Operations

## Verified Local Setup

The pinned checkout is `0.1.1-rc.2` at `b150a551`. `CI=true pnpm install`, `CI=true pnpm run build`, and `CI=true pnpm run typecheck` passed earlier on Linux x64 with Node 24.16.0 and pnpm 11.7.0. The `CI=true` install path preserved the user-owned global Git hooks configuration.

## Focused Verification

Use the installed `node_modules/.bin/vitest` entrypoint when dependencies are already present and a `pnpm exec` status check would attempt installation. Use `--config vitest.e2e.config.ts` for `.e2e.ts` Loader composition tests. Never treat a “no test files found” result as a pass.

## Brain Operations

The brain can scaffold a vault, ingest immutable sources, import an allowlisted Harness inventory, synthesize a portability report, render HTML, lint the vault, and verify a deterministic tree hash. Pin `--expected-commit` and `--as-of` for reproducible imports.

## Boundaries

Do not run live-provider, browser, native, release, or production actions merely to broaden a local evidence claim. Choose the smallest tier that answers the actual question and record what did not run.

Related: [[Keyless Architecture Verification Results]] | [[Known Limitations and Open Risks]]
