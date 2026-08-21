---
type: "concept"
title: "Security and Trust Boundaries"
domain: "DeepSeek Harness architecture, operations, extension development, security, testing, and debugging"
status: "active"
created: "2026-08-21"
updated: "2026-08-21"
tags:
  - "#domain/deepseek-harness-architecture-operations-extension-development-s"
  - "#type/concept"
  - "#confidence/evidence-based"
confidence: "evidence-based"
related:
  - "[[DeepSeek Harness System Dissection]]"
  - "[[DeepSeek Harness Review Verdict]]"
  - "[[Tool execution and policy pipeline]]"
  - "[[Defensive lifecycle and concurrency patterns]]"
  - "[[Capability seam design]]"
  - "[[Testing evidence tiers]]"
  - "[[Security and Trust Review Flow]]"
  - "[[Known Limitations and Open Risks]]"
  - "[[Installation and Operations]]"
source_urls:
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/bundle/base/cordis.patch.yml"
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md"
  - "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md"
---

# Security and Trust Boundaries

DeepSeek Harness does not have one master security switch. Its protection model is layered across tool policy, approval, permission presets, sandboxing, filesystem observation, subprocess ownership, environment scrubbing, credential resolution, host trust, storage, and durable logging. A review must trace the complete execution path.

## Control Map

| Control | Owner | Primary question |
|---|---|---|
| Tool registry and guards | `dsh-tools` | Can this named tool execute this call? |
| Approval | `dsh-user-approval` | Does this one-shot ask receive human authorization? |
| Permission presets | `dsh-permission-presets` | Which sandbox and approval modes are paired? |
| Sandbox policy | `dsh-sandbox-policy` | Which filesystem and process effects are permitted? |
| Sandbox provider | local or remote provider | How is the policy enforced for the execution world? |
| Filesystem observation | `dsh-fs-observation-policy` | Was a file observed before edit or write intent? |
| Subprocess service | local or E2B provider | How are process groups, signals, output, and teardown owned? |
| Credentials | credential service and provider | Where are secret values resolved and redacted? |
| Web trusted hosts | Web runtime and connection | Which authorities may reach the bound service? |
| Session log | session and persistence | What model-visible and tool-visible facts remain auditable? |

## Default Permission Posture

The base bundle sets sandbox mode from `DSH_PERMISSION_MODE`, defaulting to `workspace-write`. Approval defaults to `ask` unless the mode is `danger-full-access`, in which case it becomes `never`. The permission preset registry exposes `read-only`, `workspace-write`, and `danger-full-access` pairings.

This is a default composition fact, not a permanent guarantee. Later profile, home, or invocation patches can replace the row's complete configuration. Always inspect the effective tree when a deployment matters.

## Tool Enforcement Path

The model does not directly invoke a tool body. The loop records the call, then the tools runtime applies pre-execute policy. An ask decision routes through approval. Monotonic guards run after approval and can deny but must not be bypassed by reordering. The execute waterfall wraps the body. Post-execute can block or replace results. Definition finalization enforces content invariants. The final result notification observes a frozen authoritative outcome.

The critical security property is enforcement in the operation that makes the decision. Removing a schema from the prompt or hiding a button is not authorization. Alternate callers must still reach the same executor denial.

## Filesystem Boundary

Filesystem access is a capability seam. A provider owns path operations. Model-facing tools consume it. Filesystem-specific intent events allow observation and policy plugins to enforce read-before-edit rules for mutation tools.

Workspace-write is a policy scope, not proof that every path calculation is safe. Reviews must inspect path normalization, symlink handling, provider root selection, and subprocess access to the same filesystem world.

The defensive guide specifically requires unlinking link-shaped paths rather than recursively removing them. Recursive deletion is reserved for known real directories because junctions and symlinks may otherwise redirect the operation.

## Process Boundary

The subprocess service owns child process groups, output, signals, and settlement. Sandbox consumers may wrap command arguments before spawning. Shell and terminal capabilities sit above this layer.

The defensive guide requires spawned commands to receive a scrubbed environment that removes key, secret, token, and password variables. Temporary and spill files use private directories, unpredictable names, exclusive creation, and owner-only modes.

Timeout, signal, and exit code are orthogonal outcomes. A process that traps a timeout signal and exits zero is still timed out. Reporting only exit code would create a false success.

Disposal must wait for quiescence. Issuing a kill without awaiting child exit can leave orphan work after the owning plugin is gone.

## Credential Boundary

Credentials are resolved through a dedicated service and local provider. The source checkout may read environment values, a gitignored root `.env`, or a Harness credential document. Composition files refer to credential names or providers rather than embedding secrets.

The brain must never copy secret values. A source note may name `DEEPSEEK_API_KEY` as a required variable, but it must not inspect or preserve its value.

Settings and API surfaces require redaction review because a secret can leak through diagnostics, serialization, telemetry, or client projection even if execution itself is safe.

## Web Boundary

The Web server defaults to `127.0.0.1:3080`. The Web runtime derives trusted hosts from the active bind and explicit additions. The connection plugin uses that set for API transport trust.

Loopback default reduces exposure but is not authentication. A deployment that binds more broadly must review trusted hosts, reverse-proxy behavior, network reachability, browser origin handling, and any credentials or session data exposed through the gateway.

## Durable Audit Boundary

Session events provide durable evidence for turns, steps, user messages, assistant chunks and anchors, tool calls, and tool results. Live events control work but are not automatically replay facts.

The `model-visible implies logged` rule makes session reconstruction a security and audit property. A policy or plugin that injects model-visible data without a durable event would create an invisible influence and violate the architecture.

Durability is not equivalent to confidentiality. Persistence roots, telemetry exports, session search, attachments, spill files, and logs each require their own retention and access review.

## Subagent and Workflow Boundary

Subagents can run in process or through external transports. Jobs can continue in the background. Workflows can execute model-authored orchestration in worker threads. Each mechanism crosses an ownership or execution boundary.

The parent must retain explicit identity, authority, cancellation, collection, and teardown semantics. Ambient initiator identity is process-local and must be materialized across workers, processes, HTTP, or durable queues.

## Strengths Observed

- Security-relevant services are explicit rather than hidden in the loop.
- Tool guards are monotonic owner policy.
- Approval is one-shot and sits before non-bypassable guards.
- Tool results become immutable before durable recording.
- Environment scrubbing and private temporary-file guidance are documented.
- Disposal and callback containment are treated as security-relevant lifecycle behavior.
- Model-visible state is designed for durable reconstruction.
- Permission presets make the sandbox and approval pairing visible.

## Risks and Unknowns

- No claim is made that the review found no vulnerabilities.
- The complete implementation of every filesystem, process, Web, credential, and storage provider was not line-audited.
- Browser origin behavior was not exercised.
- Remote E2B execution was not tested.
- Native Landlock behavior was not executed.
- Danger-full-access is intentionally dangerous and disables approval in the shipped preset.
- Later patch layers can replace default policy configuration.
- Telemetry is disabled by default in the base row, but enabled deployments need separate privacy review.
- Provider-specific errors and metadata need redaction review before exposing a gateway outside its intended trust context.

## Review Procedure

1. Dump the effective composition.
2. Identify the model-facing tool and its execution mode.
3. Trace pre-execute policy, approval, guards, body, post-execute, finalization, and result recording.
4. Trace filesystem and subprocess providers used by the body.
5. Identify all credential, setting, and environment reads.
6. Identify durable events, persistence, telemetry, and client projections.
7. Test denial through the executor, not presentation.
8. Verify the denied body made no external change.
9. Dispose the owning plugin and verify quiescence.
10. Record untested platform or provider behavior as unknown.

Use [[Security and Trust Review Flow]] and [[Verification Tier Selection Flow]].

## Sources

- [Base permission composition](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/bundle/base/cordis.patch.yml)
- [Tool execution pipeline](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/tool-execution-pipeline.md)
- [Defensive patterns](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/defensive-patterns.md)
- [Repository agent rules](https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/AGENTS.md)

## Confidence

Evidence-based for the documented architecture and pinned default composition. Practitioner for the review procedure. Unknown for unexecuted platform, remote-provider, and browser controls.
