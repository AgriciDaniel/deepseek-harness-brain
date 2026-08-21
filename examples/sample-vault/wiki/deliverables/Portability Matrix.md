---
type: "deliverable"
title: "Portability Matrix"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags: ["#domain/deepseek-harness-architecture-operations-extension-development-s", "#type/deliverable", "#confidence/practitioner"]
confidence: "practitioner"
related: ["[[Cordis Fork Delta]]", "[[Keyless Architecture Verification Results]]", "[[Action Roadmap]]", "[[wiki/deliverables/_index|Deliverables Hub]]"]
source_urls: ["https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages", "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/architecture.md"]
---

# Portability Matrix

The rank is practitioner advice. “Observed” means every curated evidence path was present in the pinned checkout, not that a destination application is compatible.

| Rank | Subsystem | Minimal slice | Recommendation |
|---:|---|---|---|
| 5 | Session events and request reconstruction | Typed append-only events, immutable snapshots, message derivation, reconstruction invariant | Port first as agent history authority |
| 5 | Tool execution | Registry, pre-policy, approval, guards, execution, final result, cancellation | Port before mutating tools |
| 5 | Capability seams | Neutral definition, provider, consumer, fake, disposal | Adopt for replaceable or security-sensitive capabilities |
| 5 | Approval | One-shot decision, audit pair, cancellation, fail closed | Keep inside the operation path |
| 5 | Effect ownership | Ownership-first setup, disposer stack, child quiescence | Port the rules before the Cordis framework |
| 4 | Session projections | Pure reducer, replay, versioned advisory checkpoint | Add after the event log |
| 4 | Prompt assembly | Ordered sections, strict variables, effective tool schemas | Add after the tool registry |
| 4 | LLM runtime | Adapter registry, prepared route, cancellation, normalized errors | Add for multiple providers or hot routes |
| 4 | Persistence | Create, append, load, flush, contiguity, format version | Port a small provider first |
| 4 | Sandbox contract | Per-call mode, root, evidence, fail-closed unsupported host | Port the contract, choose platform providers separately |
| 3 | Subagents | Named provider, typed one-shot result, holder, disposal | Add only for a concrete bounded delegation use case |
| 3 | Loader reconciliation | Prepare, settle, commit, restore, aggregate rollback failure | Add only when live reload is required |
| 2 | Profiles and bundles | Ordered composition, full replacement, effective dump | Prefer simpler explicit composition first |
| 2 | Workflows | Bounded application-owned DAG, typed terminal results | Avoid model-authored JavaScript by default |
| 2 | Web contracts | Exact codecs, stable errors, transport-owned trust | Prefer conventional schemas unless generated RPC is required |

Use `references/portability-rules.json` and the checkout adapter for the machine-readable paths, risks, and required tests.

Related: [[Cordis Fork Delta]] | [[Capability seam design]] | [[Tool execution and policy pipeline]]
