---
type: "source"
title: "agent-lifecycle"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/agent-lifecycle.md"
sources:
  - ".raw/sources/agent-lifecycle.md"
---

# agent-lifecycle

## Source

- Path: `.raw/sources/agent-lifecycle.md`
- Hash: `348a63eebf0e704a44c9ececd22a4ebcbf0691161ab4a81790f96f7d4a743f9d`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- A step is one model request plus its tool calls.
- A turn contains zero or more steps and can close after rejection without a model request.
- The pre-step waterfall receives the authoritative entered message batch.
- Session events carry replayable transcript facts.
- Agent events coordinate inbox, status, interception, steering, continuation, and errors.

Supports [[DeepSeek Harness System Dissection]] and [[Turn and Tool Trace Flow]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
