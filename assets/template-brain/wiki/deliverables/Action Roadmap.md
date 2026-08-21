---
type: "deliverable"
title: "Action Roadmap"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/deliverable", "#confidence/practitioner"]
confidence: "practitioner"
related: ["[[Portability Matrix]]", "[[Keyless Architecture Verification Results]]", "[[Health Scorecard]]", "[[Approval Queue]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e"]
---

# Action Roadmap

## First Port Recommendation

1. Select one existing application and map its current history, tool, approval, dependency-injection, and persistence contracts.
2. Port session events and request reconstruction as an isolated slice.
3. Add the guarded tool pipeline and explicit approval before any mutating tool.
4. Express capability seams through the application’s existing dependency model before considering Cordis.
5. Require focused invariants plus one assembled crossing, and preserve the proof boundary in a verification ledger.

## Later

Port projections, prompt assembly, the provider-neutral LLM seam, and a small persistence provider only as concrete needs appear. Defer dynamic profiles, model-authored workflows, and generated Web RPC until their complexity is justified.

## Refresh Trigger

When the upstream commit changes, refresh the source inventory, Cordis delta, portability support paths, focused experiments, sample hash, and audits.

Related: [[Health Scorecard]] | [[Approval Queue]] | [[Known Limitations and Open Risks]]
