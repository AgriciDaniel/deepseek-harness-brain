---
type: "source"
title: "Base Cordis Patch"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/bundle/base/cordis.patch.yml"
sources:
  - ".raw/sources/cordis.patch.yml"
---

# Base Cordis Patch

## Source

- Path: `.raw/sources/cordis.patch.yml`
- Hash: `9870a518274194c0e1ebd870cee2737fbc2ffc04ae36887871ffe6fcf74beac1`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- The base bundle inserts shared services, providers, tools, policy, persistence, compaction, subagent, workflow, and search rows.
- Later bundle and user layers target rows by id.
- A replaced row receives a complete config rather than a deep merge.
- Default permission mode is workspace-write with ask approval.
- Danger-full-access pairs unrestricted sandboxing with never approval.

Supports [[Profile, bundle, and patch-layer configuration]] and [[Security and Trust Boundaries]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
