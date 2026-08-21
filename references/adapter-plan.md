# DeepSeek Harness Brain Adapter Plan

Status: implemented and focused-test verified on 2026-08-21.

## Raw Input Types

- The installed deepseek-ai/deepseek-harness checkout at pinned commit b150a551b8d465e31e418e1b2eaf5e79bbb7d28e
- Repository-owned architecture, lifecycle, capability, testing, configuration, security, package, and user documentation
- Repository source and tests for core session, agent, agent-loop, system-prompt, tools, LLM, sandbox, approval, persistence, boot, and client packages

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No claim that a keyless, static, build, snapshot, browser, or real-API check proves a stronger tier than it actually ran
- No invented package behavior, event semantics, defaults, compatibility promise, vulnerability, benchmark, or release status
- No credentials, tokens, cookies, private settings, or local secret values in brain artifacts
- No instruction to weaken sandbox, approval, host-trust, or credential boundaries merely to make a command pass
- No mutation, publication, deployment, account change, or production action from this advisory brain
- No reliance on archived Agent Notes as current authority when source or current documentation disagrees

## Completion Gate

The domain-specific importer, portability synthesis, HTML renderer, sanitized
checkout fixture, schema pack, and focused tests now replace the generic
scaffold. Demo verification remains a separate deterministic sample gate.
