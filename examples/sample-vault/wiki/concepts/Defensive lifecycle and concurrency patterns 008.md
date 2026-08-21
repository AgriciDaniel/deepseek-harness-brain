---
type: "concept"
title: "Defensive lifecycle and concurrency patterns"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags:
  - "#domain/deepseek-harness-architecture-operations-extension-development-s"
  - "#type/concept"
  - "#confidence/evidence-based"
confidence: "evidence-based"
related:
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Claim Verification Flow]]"
  - "[[Index]]"
  - "[[Dashboard]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
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

# Defensive lifecycle and concurrency patterns

## What It Says

- Orthogonal outcomes such as timeout, signal, and exit code must be reported independently.
- Disposal must reach quiescence rather than merely request cancellation.
- Spawned commands receive a scrubbed environment and private unpredictable temporary paths.

## Source

Source: [Defensive lifecycle and concurrency patterns](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md); type official; retrieved 2026-08-21; refresh_due 2026-09-20.



## Canon Backlink

- Canon ledger entry: [references/canon/008-defensive-lifecycle-and-concurrency-patterns.md](../../references/canon/008-defensive-lifecycle-and-concurrency-patterns.md)
- Source ledger: `references/source-ledger.json`

## Related

- [[Claim Verification Flow]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
