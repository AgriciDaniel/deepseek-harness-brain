---
type: "experiment"
title: "Dispose a plugin contribution and verify its service, registry, listener, or too"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "complete"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/experiment", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Keyless Architecture Verification Results]]", "[[Defensive lifecycle and concurrency patterns]]", "[[Tool execution and policy pipeline]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/core/tools/tests/tools.spec.ts"]
---

# Dispose a plugin contribution and verify its service, registry, listener, or too

PASS on 2026-08-21: one selected test, 135 skipped by the name filter. The returned registration disposer removed the tool.

This narrow test does not prove quiescent disposal for every plugin or in-flight capability. See [[Keyless Architecture Verification Results]].
