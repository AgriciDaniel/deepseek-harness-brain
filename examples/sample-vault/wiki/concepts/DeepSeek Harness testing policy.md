---
type: "concept"
title: "DeepSeek Harness testing policy"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"
---

# DeepSeek Harness testing policy

## What It Says

- Unit, coverage, real-API, transcript snapshot, and browser snapshot tiers prove different things.
- The coverage gate requires per-file 100 percent on package source but is explicitly insufficient by itself.
- Product-visible plugins require a real Loader composition test and built entrypoints require built-artifact smokes.

## Source

Source: [DeepSeek Harness testing policy](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md); type official; retrieved 2026-08-21; refresh_due 2026-09-20.



## Canon Backlink

- Canon ledger entry: [references/canon/009-deepseek-harness-testing-policy.md](../../references/canon/009-deepseek-harness-testing-policy.md)
- Source ledger: `references/source-ledger.json`

## Related

- [[Claim Verification Flow]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
