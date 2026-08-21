---
type: "source"
title: "tool-execution-pipeline"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags:
  - "#domain/deepseek-harness-architecture-operations-extension-development-s"
  - "#type/source"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Source Manifest Guide]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[Source Intake Workflow]]"
source_urls:
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md"
sources:
  - ".raw/sources/tool-execution-pipeline.md"
---

# tool-execution-pipeline

## Source

- Path: `.raw/sources/tool-execution-pipeline.md`
- Hash: `4f2f0a8459db2da876c445bb86d66d909b8f648c2c03855217274d8067cad243`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- The loop records a tool call before execution.
- Pre-execute policy and approval run before monotonic guards.
- The execute waterfall wraps the tool body.
- Post-execute and definition finalization produce one normalized outcome.
- Final result observation is immutable before the durable model-facing result is recorded.

Supports [[Tool execution and policy pipeline]] and [[Security and Trust Boundaries]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
