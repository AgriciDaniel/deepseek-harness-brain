---
type: "source"
title: "defensive-patterns"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md"
sources:
  - ".raw/sources/defensive-patterns.md"
---

# defensive-patterns

## Source

- Path: `.raw/sources/defensive-patterns.md`
- Hash: `919d27a033c655ea6187496872caa4aa9babf08d87179562ca23545301108bb1`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- Timeout, signal, and exit code must be reported independently.
- Public outcomes are normalized at the owning service boundary.
- Agent idle status is not per-message completion.
- Disposal must wait for child work to reach quiescence.
- Untrusted output receives a scrubbed environment and private unpredictable paths.
- Link-shaped paths are unlinked rather than recursively traversed.

Supports [[Defensive lifecycle and concurrency patterns]], [[Security and Trust Boundaries]], and [[Known Limitations and Open Risks]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
