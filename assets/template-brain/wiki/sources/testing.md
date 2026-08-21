---
type: "source"
title: "testing"
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
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"
sources:
  - ".raw/sources/testing.md"
---

# testing

## Source

- Path: `.raw/sources/testing.md`
- Hash: `f47370270ceee93392660f8982c8e293883c1dd2cb625e580814a67474660036`
- Retrieved: 2026-08-21
- Type: official

## Compiled Truth

- Unit, coverage, real Loader composition, built, transcript snapshot, browser snapshot, and real-API checks prove different things.
- Per-file coverage is required but explicitly insufficient by itself.
- Product-visible plugins need a real assembled-composition test.
- Built binaries and package entrypoints must be tested under their published runtime.
- External effects are re-observed rather than accepted from model self-report.

Supports [[Testing evidence tiers]] and [[Verification Tier Selection Flow]].

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
