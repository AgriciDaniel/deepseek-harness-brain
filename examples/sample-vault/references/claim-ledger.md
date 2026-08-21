# Claim Ledger

Generated 2026-08-21 for upstream commit `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`.

Policy: every material claim names a pinned source locator and evidence tier. A local command result is observation evidence for this machine, not an upstream promise.

Second-source policy: security, compatibility, current-release, comparative, numeric, and externally observable behavior claims require an independent second source or remain visibly SINGLE-SOURCE.

| ID | Claim | Confidence | Verdict | Primary source | Second source or limit |
|---|---|---|---|---|---|
| C001 | The reviewed checkout is DeepSeek Harness `0.1.1-rc.2` at commit `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`. | evidence-based | ACCEPTED | `dsh-repository`, root `package.json` | Local `git rev-parse HEAD` and package manifest agree |
| C002 | DeepSeek Harness is developer preview and permits compatibility-breaking changes. | evidence-based | ACCEPTED | `dsh-root-readme` | `dsh-agent-orders` describes pre-release on-disk compatibility posture |
| C003 | Every major product component is a Cordis plugin and new behavior normally belongs on extension points. | evidence-based | ACCEPTED | `dsh-architecture` | `dsh-agent-orders` and `dsh-agent-loop-contract` agree |
| C004 | A step is one model request plus its tools, and a turn contains zero or more steps. | evidence-based | ACCEPTED | `dsh-agent-lifecycle` | `dsh-architecture` and `dsh-agent-loop-contract` agree |
| C005 | Model-visible request history is derived from durable session events. | evidence-based | ACCEPTED | `dsh-architecture` | `dsh-agent-orders` requires model-visible inputs to be logged |
| C006 | A capability seam requires Service Definition, Service Provider, and Consumer roles. | evidence-based | ACCEPTED | `dsh-architecture` | `dsh-capability-seams` and `dsh-agent-orders` agree |
| C007 | Tool execution applies pre-execute policy, approval, monotonic guards, execution, post-execute, finalization, and immutable result observation. | evidence-based | ACCEPTED | `dsh-tool-pipeline` | `dsh-agent-orders` names the same pipeline and enforcement rule |
| C008 | The shipped base composition defaults to workspace-write sandbox mode and ask approval. | evidence-based | ACCEPTED | `dsh-base-composition` | `dsh-agent-orders` documents the sandbox and approval services; later patches may override the default |
| C009 | Unit, coverage, real-composition, built, snapshot, browser, and real-API tiers prove different surfaces. | evidence-based | ACCEPTED | `dsh-testing-policy` | Root scripts expose separate commands and `dsh-agent-orders` forbids evidence inflation |
| C010 | The pinned repository requires Node `^22.19.0 || >=24.0.0` and pnpm `11.7.0`. | evidence-based | ACCEPTED | `dsh-development-guide` | Root package manifest agrees |
| C011 | The complete source build passes on this Linux x64 host with Node 24.16.0 and pnpm 11.7.0. | evidence-based | ACCEPTED-LOCAL | Local command `CI=true pnpm run build`, exit 0 on 2026-08-21 | Does not prove another platform, live provider, browser journey, or release package |
| C012 | The tracked checkout contains 7,903 files, 51,116,248 tracked bytes, 2,734 TypeScript or TSX files, 2,506 Markdown files, and 234 main package manifests. | evidence-based | ACCEPTED-LOCAL | Local `git ls-files`, `stat`, and count commands on 2026-08-21 | Volatile inventory, refresh on any commit change |
| C013 | Sandbox, approval, filesystem observation, subprocesses, credentials, and Web host trust are separate controls. | evidence-based | ACCEPTED | `dsh-capability-seams` | `dsh-tool-pipeline`, `dsh-base-composition`, and `dsh-defensive-patterns` provide independent control-path evidence |
| C014 | Disposal must wait for quiescence and callback failures must be contained by the dispatcher. | evidence-based | ACCEPTED | `dsh-defensive-patterns` | `dsh-agent-loop-contract` documents owned teardown and convergence |
| C015 | Real-provider behavior was verified in this review. | evidence-based | REJECTED | No live provider command was run | The build is keyless and cannot support this claim |
| C016 | The Web UI was browser-verified in this review. | evidence-based | REJECTED | No Web server or browser test was run | Vite build success proves assets compile, not interaction or visual behavior |
| C017 | The reviewed repository is free of security vulnerabilities. | contested | UNSUPPORTED | No exhaustive security audit exists in this work | [[Security and Trust Boundaries]] maps controls but explicitly refuses a clean bill of security |
| C018 | The vendored Cordis surface is materially forked from the versions recorded in `vendor/README.md`, not merely renamed. | evidence-based | ACCEPTED | `dsh-vendor-ledger`, local package manifests | `dsh-cordis-fiber` and `dsh-loader-reconciliation` expose local lifecycle and reconciliation behavior; the unavailable auxiliary fork prevents an exhaustive historical diff |
| C019 | Cordis-style effect ownership can reach quiescent disposal across child scopes and in-flight work. | evidence-based | ACCEPTED | `dsh-cordis-fiber` | `dsh-defensive-patterns` independently states the quiescence requirement |
| C020 | Loader reconciliation is rollback-covered, but it is not strictly atomic because restoration can fail. | evidence-based | ACCEPTED | `dsh-loader-reconciliation` | Failure aggregation in the implementation is direct counterevidence to an unconditional atomicity claim |
| C021 | The `!!js` configuration form evaluates JavaScript and therefore belongs only in a trusted configuration boundary. | evidence-based | ACCEPTED | `dsh-include-config` | This review did not execute untrusted configuration or claim a sandbox around evaluation |
| C022 | Session append stores contiguous immutable event snapshots and the agent loop checks model-request reconstruction. | evidence-based | ACCEPTED | `dsh-session-runtime` | `dsh-request-invariant` provides the separate loop-side invariant |
| C023 | A pre-execute denial short-circuits a tool body before execution and the pipeline exposes one final model-facing result. | evidence-based | ACCEPTED | `dsh-tools-runtime` | `dsh-tool-pipeline` documents the same ordering; focused test evidence is recorded separately |
| C024 | Prompt and tool-schema contributions are ordered and disposable, reducing prompt-to-executor drift when used through one registry. | evidence-based | ACCEPTED | `dsh-prompt-runtime` | The portability recommendation remains practitioner synthesis, not an upstream compatibility promise |
| C025 | A prepared LLM call binds one adapter route before dispatch. | evidence-based | ACCEPTED | `dsh-llm-runtime` | No live provider call was run, so provider availability and output quality remain unverified |
| C026 | Persistence has an explicit flush boundary, but this review does not prove operating-system crash durability. | evidence-based | ACCEPTED | `dsh-persistence-runtime` | Absence of a provider-specific fsync proof blocks the stronger claim |
| C027 | Approval, sandbox, filesystem authority, and transport authentication are distinct boundaries. | evidence-based | ACCEPTED | `dsh-approval-runtime`, `dsh-sandbox-runtime` | `dsh-capability-seams` and `dsh-api-gateway` show separate service ownership |
| C028 | One-shot subagents publish typed runs with explicit ownership and disposal, but should be ported only for a concrete bounded delegation use case. | practitioner | ACCEPTED-WITH-BOUNDARY | `dsh-subagent-runtime` | The implementation claim is sourced; the porting priority is practitioner judgment |
| C029 | The full historical Cordis fork delta has been reconstructed. | contested | REJECTED | The recorded upstream table and local source permit a material delta, not complete history | The auxiliary fork URL was unavailable during review and no exhaustive commit-by-commit comparison was performed |

## Interpretation Rule

`ACCEPTED` applies to the pinned source baseline. `ACCEPTED-LOCAL` applies only to the observed machine and command. `REJECTED` means direct counterevidence exists. `UNSUPPORTED` means the review does not contain enough evidence to make the claim.
