---
type: "concept"
title: "Tool execution and policy pipeline"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Capability seam design]]", "[[Keyless Architecture Verification Results]]", "[[Security and Trust Boundaries]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/core/tools/src/index.ts"]
---

# Tool execution and policy pipeline

The portable invariant is one enforceable path: registry lookup, pre-execute policy, one-shot approval, monotonic guards, execution, post-execute rewriting, finalization, then immutable result observation. A denial must short-circuit before the body. Each call exposes one model-facing final result.

Keep authorization in this execution path, not only in prompts or UI. Compose cancellation sources, drain work that already started, freeze final observations, and make registration reversible.

Related: [[Keyless Architecture Verification Results]] | [[Portability Matrix]]
