---
type: "concept"
title: "Testing evidence tiers"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Keyless Architecture Verification Results]]", "[[Action Roadmap]]", "[[Known Limitations and Open Risks]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"]
---

# Testing evidence tiers

Unit, coverage, source-level integration, real Loader composition, built entrypoint, transcript snapshot, browser snapshot, native, and real-provider tests answer different questions. A narrow pass never upgrades itself into a broader tier.

For portable subsystem work, require the smallest focused invariant tests plus one assembled crossing that exercises the real registration and disposal path. Record skipped tests, filtered tests, host limits, and commands that never reached the runner.

Related: [[Keyless Architecture Verification Results]] | [[Portability Matrix]]
