---
type: "source"
title: "development"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/development.md"
sources:
  - ".raw/sources/development.md"
---

# development

## Source

- Path: `.raw/sources/development.md`
- Hash: `b7eb2eb7cd8b871dc61e5c734f66b0f505e3315f077c3c679d9f5a286be2bd30`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- Node 22.19 or newer in the 22 line, or Node 24 and later, is required.
- pnpm 11.7.0 is pinned through Corepack.
- Host and Client TypeScript programs remain separate because their Cordis Context declarations collide in one program.
- Host build and Typert generation precede Client compilation.
- Public typecheck is the documented first-time setup completion check.

Supports [[Installation and Operations]] and [[DeepSeek Harness System Dissection]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
