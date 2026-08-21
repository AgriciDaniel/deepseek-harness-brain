# Product Boundaries

DeepSeek Harness Brain is an advisory, read-only Obsidian brain for DeepSeek Harness architecture, operations, extension development, security, testing, and debugging.

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No claim that a keyless, static, build, snapshot, browser, or real-API check proves a stronger tier than it actually ran
- No invented package behavior, event semantics, defaults, compatibility promise, vulnerability, benchmark, or release status
- No credentials, tokens, cookies, private settings, or local secret values in brain artifacts
- No instruction to weaken sandbox, approval, host-trust, or credential boundaries merely to make a command pass
- No mutation, publication, deployment, account change, or production action from this advisory brain
- No reliance on archived Agent Notes as current authority when source or current documentation disagrees

## Safety Risks

- Developer-preview churn makes package names, defaults, events, and on-disk formats stale quickly
- Everything-is-a-plugin flexibility can hide load-order, ownership, disposal, and cross-capability integration failures
- A green unit suite can miss broken Loader composition, built entrypoints, browser output, or real-provider behavior
- Permission, sandbox, approval, filesystem, subprocess, and credential layers can be confused as one control even though they are separate
- Generated catalogs and bilingual derivatives may drift if hand-edited instead of regenerated through repository gates
- Local build artifacts may be mistaken for tracked source or current release evidence

## Release Boundary

Version 0.2.0 is community-ready. The source and adapter gates, deterministic
sample vault, source citations, graph checks, license and attribution review,
privacy scans, and community packaging pipeline pass. Market-ready remains false
because browser, live-provider, native, cross-platform, comprehensive
security-audit, and production-scale evidence remain open. Those stronger claims
require their own evidence and an explicit human-reviewed market decision.
