# Source Map

## Raw Sources

- The installed deepseek-ai/deepseek-harness checkout at pinned commit b150a551b8d465e31e418e1b2eaf5e79bbb7d28e
- Repository-owned architecture, lifecycle, capability, testing, configuration, security, package, and user documentation
- Repository source and tests for core session, agent, agent-loop, system-prompt, tools, LLM, sandbox, approval, persistence, boot, and client packages

## Enrichment Sources

- The upstream DeepSeek Harness GitHub repository and release history
- The vendored Cordis source, primer, and linked spatiotemporal composability paper
- Official Node.js, pnpm, DeepSeek API, and Agent Client Protocol documentation when a current compatibility claim requires it

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.
