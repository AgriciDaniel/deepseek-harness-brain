---
type: "concept"
title: "Defensive lifecycle and concurrency patterns"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Cordis Fork Delta]]", "[[Tool execution and policy pipeline]]", "[[Keyless Architecture Verification Results]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/vendor/cordis/src/fiber.ts"]
---

# Defensive lifecycle and concurrency patterns

Ownership must exist before setup can publish work. Disposal must be idempotent and reach quiescence, which means children and work already admitted have settled. Cancellation requests alone do not prove settlement.

Model timeout, signal, exit code, policy denial, rollback failure, and cleanup failure as orthogonal outcomes. Contain observer failures so a committed fact cannot be retroactively undone by a callback.

Related: [[Cordis Fork Delta]] | [[Keyless Architecture Verification Results]]
