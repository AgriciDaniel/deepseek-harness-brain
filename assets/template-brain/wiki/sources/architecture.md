---
type: "source"
title: "architecture"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/architecture.md"
sources:
  - ".raw/sources/architecture.md"
---

# architecture

## Source

- Path: `.raw/sources/architecture.md`
- Hash: `6a6e9d4fdb582661d2f27ad14ec4bee287ba7b764963b96964a54435662fd55b`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- Profiles stack bundles and patch layers into a Cordis plugin tree.
- Durable session events and live agent or capability events have different responsibilities.
- The turn lifecycle moves through input claim, prompt assembly, model request, tool execution, and durable closure.
- Capability seams use definition, provider, and consumer roles.
- New behavior normally attaches to a documented extension point.

Supports [[DeepSeek Harness System Dissection]], [[Capability seam design]], and [[Profile, bundle, and patch-layer configuration]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
