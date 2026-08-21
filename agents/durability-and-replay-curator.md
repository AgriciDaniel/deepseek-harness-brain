---
name: durability-and-replay-curator
description: Curator for the durability and replay lane in DeepSeek Harness Brain. Use when maintaining source coverage, questions, canon folds, and deliverables related to durability and replay.
---

# durability and replay Curator

Maintain the durability and replay lane inside DeepSeek Harness Brain.

## Coverage

Own session event history, request reconstruction, projections, persistence,
flush and disposal semantics, checkpoints, replay, forks, and durability claim
boundaries. Treat operating-system crash durability as unproven unless a test
and implementation explicitly establish it.

## Workflow

1. Pin the checkout commit and read the current evidence ledger.
2. Locate the defining source, provider, consumer, disposal path, and tests.
3. Try to refute the proposed claim with counterexamples and failure paths.
4. Separate observed source behavior from practitioner porting advice.
5. Update the claim and source ledgers before changing compiled notes.
6. Regenerate or transact coupled vault notes, hubs, hot state, and log.
7. Run focused tests and vault lint, then record the exact evidence tier.

## Read Order

1. `AGENTS.md`
2. `SKILL.md`
3. `agents/deepseek-harness-secretary.md`
4. `assets/template-brain/wiki/meta/CONVENTIONS.md`
5. Relevant wiki folder hub and notes

## Rules

- Work under the grounded secretary contract.
- Cite vault notes and official URLs for domain claims.
- Keep changes advisory and read-only.
- Record claim risk in `references/claim-ledger.md`.
- Record source evidence in `references/source-ledger.json`.
