---
type: "source"
title: "capability-seams"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/capability-seams.md"
sources:
  - ".raw/sources/capability-seams.md"
---

# capability-seams

## Source

- Path: `.raw/sources/capability-seams.md`
- Hash: `da2222f7cdabd259da3c676f9ea5e1fd0f11422f90604954c8049dba40d833ae`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- The generated graph names service declarations, providers, and direct consumers.
- Replacing a provider changes all consumers behind the same interface.
- Filesystem, subprocess, sandbox, approval, persistence, LLM, subagent, and Web services remain separate capabilities.
- Core spine services and swappable seams are visually distinguished.
- The graph is generated from current source relationships.

Supports [[Capability seam design]] and [[Security and Trust Boundaries]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
