# Current Requirements

Status: researched against the pinned upstream checkout. Refresh before relying on a newer release.

## Evidence Baseline

- Upstream repository: `deepseek-ai/deepseek-harness`
- Reviewed commit: `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Package version: `0.1.1-rc.2`
- Retrieval date: 2026-08-21
- Project stage: developer preview with compatibility-breaking changes explicitly permitted

## Installation Requirements

- Node.js `^22.19.0 || >=24.0.0`.
- Corepack-backed pnpm `11.7.0`.
- Git 2.26 or newer for the repository's optional worktree-local hooks integration.
- A successful source build before running the Web or headless profile from this checkout.
- A DeepSeek API key only for model-backed tasks and real-API tests. Keyless builds, unit tests, Loader smokes, and replay snapshots do not require it.

## Operating Requirements

- Start the Web profile with `pnpm dsh web` after the build, or run the documented headless profile for one-shot tasks.
- Keep credentials in the environment, the gitignored root `.env`, or the Harness credential store. Never put them in the brain.
- Treat profiles as ordered bundle stacks followed by user and invocation patch layers.
- Keep the default `workspace-write` sandbox and `ask` approval pairing unless the operator intentionally selects another permission preset.
- Use `dsh --profile web --dump-config` when current effective composition matters.

## Development Requirements

- Read `docs/architecture.md` before changing packages.
- Implement new behavior on plugin extension points unless the loop contract itself must change.
- Make model-visible inputs reconstructable from the durable session log.
- Register contributions as reversible Cordis effects and prove disposal.
- Design every capability as a definition, provider, and consumer set.
- Keep Host and Client TypeScript programs separate.
- Update package contracts, generated catalogs, snapshots, and Agent Notes when the affected surface requires them.

## Verification Requirements

- Select the tier that exercises the claimed behavior: unit, coverage, real Loader composition, built entrypoint, transcript snapshot, browser snapshot, or real API.
- Do not treat per-file coverage as proof of assembled behavior.
- Do not treat a self-skipped e2e suite as live-provider evidence.
- Verify effects in the external world rather than accepting the agent's own output as proof.
- Run platform-specific gates on the matching platform or report the platform gap.

## Source Log

| Source | URL | Retrieved | Version | Confidence | Use |
|---|---|---:|---|---|---|
| Repository README | https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/README.md | 2026-08-21 | 0.1.1-rc.2 | evidence-based | Product stage and run path |
| Development guide | https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/development.md | 2026-08-21 | pinned commit | evidence-based | Toolchain and build order |
| Architecture | https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/architecture.md | 2026-08-21 | pinned commit | evidence-based | Composition and lifecycle |
| Testing policy | https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/docs/testing.md | 2026-08-21 | pinned commit | evidence-based | Evidence tiers |
| Base bundle | https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/bundle/base/cordis.patch.yml | 2026-08-21 | pinned commit | evidence-based | Default services and permission policy |

## Refresh Rule

Recheck upstream HEAD, the package version, the Node engine, pnpm pin, profile patches, architecture, and testing policy on every release or material architecture change. Recheck monthly while the repository remains in developer preview.
