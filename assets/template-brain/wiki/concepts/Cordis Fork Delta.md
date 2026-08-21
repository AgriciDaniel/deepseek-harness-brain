---
type: "concept"
title: "Cordis Fork Delta"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/concept", "#confidence/evidence-based"]
confidence: "evidence-based"
related: ["[[Portability Matrix]]", "[[Defensive lifecycle and concurrency patterns]]", "[[Profile, bundle, and patch-layer configuration]]", "[[wiki/concepts/_index|Concepts Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/vendor/README.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/vendor/cordis/src/fiber.ts", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/vendor/loader/src/config/entry.ts"]
---

# Cordis Fork Delta

## Verdict

The vendored Cordis family is materially adapted, not merely renamed. The repository's provenance table records upstream Cordis `4.0.0-rc.7`, while the local package manifest is `4.0.1`. Local source adds or carries Harness-relevant lifecycle, effect ownership, loader reconciliation, and configuration behavior.

## Portable Core

- Register ownership before setup can publish work.
- Make every registration return an idempotent disposer.
- Treat cancellation and settlement as separate facts.
- Dispose children and in-flight work to quiescence.
- Prepare and settle a candidate configuration before committing it.
- Restore the last good tree on failure, while reporting restoration failure separately.

## Boundaries

Loader updates are rollback-covered, not strictly atomic. The `!!js` YAML form evaluates JavaScript and belongs only in a trusted configuration boundary. File replacement without an explicit `fsync` proof must not be described as crash durable.

This is not a complete historical fork reconstruction. The review compared the pinned local tree with its recorded provenance and behavior, but the auxiliary fork was unavailable and no commit-by-commit ancestry diff was completed.

Related: [[Portability Matrix]] | [[Keyless Architecture Verification Results]]
