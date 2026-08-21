---
type: "concept"
title: "Profile, bundle, and patch-layer configuration"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Cordis Fork Delta]]", "[[Portability Matrix]]", "[[Installation and Operations]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/architecture.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/boot/app-boot/src/profile.ts"]
---

# Profile, bundle, and patch-layer configuration

Profiles select ordered bundles and patches that assemble an initially empty plugin tree. A candidate must be fully parsed and validated before replacing the live composition, and the effective configuration needs an inspectable dump.

This is powerful and expensive. Port it only when an application needs user-selectable modes or live plugin installation. For most applications, start with explicit static composition and add reconciliation after the simpler model becomes a real constraint.

Related: [[Cordis Fork Delta]] | [[Portability Matrix]]
