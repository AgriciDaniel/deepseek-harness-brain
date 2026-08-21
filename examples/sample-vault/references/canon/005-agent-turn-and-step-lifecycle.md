---
type: "canon"
title: "005. Agent turn and step lifecycle"
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
  - "[[Agent turn and step lifecycle]]"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/agent-lifecycle.md"
---

# 005. Agent turn and step lifecycle

Ledger: 005 | source: Agent turn and step lifecycle | confidence: evidence-based | fold: [[Agent turn and step lifecycle]] | status: captured.

## What It Says

- A step contains one model request plus its tools, while a turn contains zero or more steps.
- The pre-step decision may reject the proposed step or replace the complete entered message batch.
- SDK transcript consumers should use session events, while agent events are the live coordination API.

## Source

Source: [Agent turn and step lifecycle](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/agent-lifecycle.md); type official; retrieved 2026-08-21; refresh_due 2026-09-20.

## Brain Hooks

- Folded concept: [[Agent turn and step lifecycle]]
- Source ledger: `references/source-ledger.json`
- Verification path: [[Claim Verification Flow]]
