---
type: "source"
title: "Agent Loop Package Contract"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/core/agent-loop/README.md"
sources:
  - ".raw/sources/README-d3c5d7708c5f.md"
---

# Agent Loop Package Contract

## Source

- Path: `.raw/sources/README-d3c5d7708c5f.md`
- Hash: `d3c5d7708c5faf4a7394f67e50cf12510191f4ef0fc2925e789a037e5e5f5390`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- The package is the only concrete loop driver.
- Agent creation and resume use rollback-covered publication and owned teardown.
- Follow-up, steer, and inject differ by inbox target and wake behavior.
- Successful provider calls record an assistant completion anchor.
- Parallel-safe tool bodies may overlap while policy and durable results remain model ordered.

Supports [[DeepSeek Harness System Dissection]], [[Turn and Tool Trace Flow]], and [[Defensive lifecycle and concurrency patterns]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
