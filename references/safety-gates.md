# Safety Gates

V1 is read-only and advisory unless a future release explicitly adds approved,
reversible mutation.

## Refusal Rules

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

## Release-Blocking Gates

- The pinned checkout, raw source hashes, or dated trustworthy sources are missing or stale.
- A raw source file is absent from the manifest or its recorded hash differs.
- Deliverables contain unsupported claims.
- Credentials or private client data are present.
- A mutation path exists without approval and rollback.
- Market-ready is claimed without the explicit release-status decision and broader evidence tiers.
