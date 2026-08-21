---
type: "concept"
title: "Tool execution pipeline"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md"
---

# Tool execution pipeline

## What It Says

- Tool execution runs pre-execute policy, monotonic guards, execution, post-execute rewriting, finalization, and immutable result observation.
- Approval resolves one-shot asks before monotonic owner guards.
- A single tool result is the model-facing outcome after pipeline normalization and finalization.

## Source

Source: [Tool execution pipeline](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md); type official; retrieved 2026-08-21; refresh_due 2026-09-20.



## Canon Backlink

- Canon ledger entry: [references/canon/007-tool-execution-pipeline.md](../../references/canon/007-tool-execution-pipeline.md)
- Source ledger: `references/source-ledger.json`

## Related

- [[Claim Verification Flow]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
