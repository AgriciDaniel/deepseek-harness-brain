---
type: "concept"
title: "Capability seam design"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Portability Matrix]]", "[[Tool execution and policy pipeline]]", "[[Defensive lifecycle and concurrency patterns]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/capability-seams.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/AGENTS.md"]
---

# Capability seam design

A real capability seam has three roles: a provider-neutral service definition, one or more providers, and consumers that depend only on the service. Registration and provider replacement must be disposable.

Port the pattern when a capability has multiple providers, security authority, lifecycle ownership, or testing value. Avoid a one-role abstraction that merely renames a concrete implementation. Test the provider contract, consumer integration, duplicate rejection, failure vocabulary, and disposal.

Related: [[Portability Matrix]] | [[Tool execution and policy pipeline]]
