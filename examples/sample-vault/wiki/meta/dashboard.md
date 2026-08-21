---
type: "dashboard"
title: "Dashboard"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "evergreen"
created: "2026-08-21"
updated: "2026-08-21"
tags:
  - "#domain/deepseek-harness-architecture-operations-extension-development-s"
  - "#type/dashboard"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Start Here]]"
  - "[[CONVENTIONS]]"
  - "[[Tag Taxonomy]]"
  - "[[Index]]"
  - "[[Overview]]"
  - "[[Hot]]"
  - "[[Log]]"
  - "[[Real-API behavior is not verified without a configured DeepSeek API key]]"
  - "[[Which layer owns the authoritative decision being reviewed composition, service,]]"
  - "[[Boot a keyless real Loader composition and verify the observed world rather than]]"
  - "[[Dashboard]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Synthesis Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls: []
---

# Dashboard

Dataview views over the vault require the Dataview community plugin. Without Dataview, use the linked seed lists and run `python3 scripts/audit_brain.py --json` for the same gate signals.

## Visual Map

![[brain-relationship-map.svg]]

## Notes by status

```dataview
TABLE status, domain, confidence, updated
FROM "wiki"
WHERE type != "meta"
SORT status ASC, updated DESC
```

## Seeds needing substance

```dataview
LIST
FROM "wiki"
WHERE status = "seed"
SORT file.name ASC
```

## Contested and low-confidence claims

```dataview
LIST
FROM "wiki"
WHERE confidence = "contested" OR contains(tags, "#confidence/contested") OR contains(tags, "#confidence/folklore")
SORT updated DESC
```

## Recently updated

```dataview
TABLE updated, status, confidence
FROM "wiki"
SORT updated DESC
LIMIT 15
```

## Seed Evidence Queue

### Gaps

- [[Real-API behavior is not verified without a configured DeepSeek API key]]
- [[Browser interaction and visual behavior require a running Web profile and browse]]
- [[Platform-specific behavior outside Linux x64 requires the matching CI or native]]
- [[Evidence Coverage Not Yet Verified]]

### Questions

- [[Which layer owns the authoritative decision being reviewed composition, service,]]
- [[What durable event or external observation proves the claimed behavior]]
- [[Which failure or counterexample would refute the leading interpretation]]
- [[Does the selected verification tier exercise source, built artifacts, assembled]]
- [[What Current Official Source Resolves The Highest Risk Claim]]

### Experiments

- [[Boot a keyless real Loader composition and verify the observed world rather than]]
- [[Reconstruct a model request from session events and compare it with the frozen r]]
- [[Dispose a plugin contribution and verify its service, registry, listener, or too]]
- [[Deny a mutating tool through the executor and verify the body did not run]]
- [[Source To Claim Spot Check Probe]]

Watch for `> [!gap]`, `> [!question]`, `> [!contradiction]`, `> [!stale]`, and `> [!done]` callouts in seed notes.

## Operating Links

- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Explore Plan Code Commit]]
- [[Multi-Agent Fan-Out Research Flow]]
- [[Context Compaction Routine]]
- [[Synthesis Workflow]]
- [[Reporting Workflow]]
- [[Approval Queue]]
- [[Health Scorecard]]
- [[Action Roadmap]]
