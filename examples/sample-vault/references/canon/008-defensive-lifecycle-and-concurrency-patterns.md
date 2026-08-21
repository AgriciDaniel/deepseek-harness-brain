---
type: "canon"
title: "008. Defensive lifecycle and concurrency patterns"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags:
  - "#domain/deepseek-harness-architecture-operations-extension-development-s"
  - "#type/canon"
  - "#confidence/evidence-based"
confidence: "evidence-based"
related:
  - "[[Defensive lifecycle and concurrency patterns 008]]"
  - "[[Index]]"
  - "[[Dashboard]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Synthesis Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
source_urls:
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md"
---

# 008. Defensive lifecycle and concurrency patterns

Ledger: 008 | source: Defensive lifecycle and concurrency patterns | confidence: evidence-based | fold: [[Defensive lifecycle and concurrency patterns 008]] | status: captured.

## What It Says

- Orthogonal outcomes such as timeout, signal, and exit code must be reported independently.
- Disposal must reach quiescence rather than merely request cancellation.
- Spawned commands receive a scrubbed environment and private unpredictable temporary paths.

## Source

Source: [Defensive lifecycle and concurrency patterns](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md); type official; retrieved 2026-08-21; refresh_due 2026-09-20.

## Brain Hooks

- Folded concept: [[Defensive lifecycle and concurrency patterns 008]]
- Source ledger: `references/source-ledger.json`
- Verification path: [[Claim Verification Flow]]
