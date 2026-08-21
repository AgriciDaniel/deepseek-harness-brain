---
type: "gap"
title: "Known Limitations and Open Risks"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/gap", "#confidence/contested"]
confidence: "contested"
related: ["[[DeepSeek Harness Review Verdict]]", "[[Portability Matrix]]", "[[Cordis Fork Delta]]", "[[Testing evidence tiers]]", "[[Action Roadmap]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/README.md", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md"]
---

# Known Limitations and Open Risks

- Developer preview permits breaking changes. Every port must pin the source commit and own its copied contract.
- The Cordis delta is material but not exhaustively reconstructed. The auxiliary fork was unavailable.
- Loader changes are rollback-covered, not strictly atomic. Rollback can fail.
- `!!js` evaluates JavaScript and is trusted configuration only.
- Persistence flush semantics do not prove operating-system crash durability without provider-specific evidence.
- File-effect sandboxing does not by itself prove hostile-code isolation.
- Dynamic profiles, HMR, workflows, and generated RPC add substantial lifecycle and packaging complexity.
- Browser, live-provider, native, cross-platform, security-audit, full release-matrix, and production-load evidence are absent.
- Brainstein C8.3 has both a configured-vault path mismatch in version 1.2.0 and a legitimate unmet 60-citation market-research threshold.
- The brain's deterministic and keyless checks support internal demo verification only. Market-ready remains explicitly false.

Related: [[Keyless Architecture Verification Results]] | [[Action Roadmap]] | [[Health Scorecard]]
