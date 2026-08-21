---
type: "experiment"
title: "Deny a mutating tool through the executor and verify the body did not run"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "complete"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/experiment", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Keyless Architecture Verification Results]]", "[[Tool execution and policy pipeline]]", "[[Security and Trust Boundaries]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/core/tools/tests/tools.spec.ts"]
---

# Deny a mutating tool through the executor and verify the body did not run

PASS on 2026-08-21: one selected test, 135 skipped by the name filter. The pre-execute denial short-circuited before the tool body.

This does not prove every policy provider, approval UI, sandbox provider, or mutating tool. See [[Keyless Architecture Verification Results]].
