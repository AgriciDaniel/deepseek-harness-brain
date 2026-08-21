# Publishing Notice

DeepSeek Harness Brain 0.2.0 is public under its community-ready distribution
requirements. Public availability does not prove that every future release or
market-readiness requirement has passed.

## Rights boundary

Public availability alone does not grant redistribution rights. This repository
may include original synthesis, pinned public links, compliant short quotations,
and reviewed captures from MIT-licensed DeepSeek Harness files. The upstream MIT
license and attribution must remain with those captures.

Do not add screenshots, site artwork, account exports, prompt histories, client
notes, or third-party documents unless their public reuse rights are explicit.

## Repository-safe material

- Original summaries, diagrams, code, scripts, and generated project artwork.
- Pinned links and hashes for official public sources.
- The committed allowlist of public upstream captures recorded in the raw manifests.
- Sanitized examples with obvious placeholders.

## Material that must stay private

- Credentials, tokens, cookies, OAuth material, `.env` files, or private keys.
- Client-specific or account-derived `.raw/` captures and manifests.
- Local paths, private user data, personal conversation history, or runtime logs.
- `.transactions/`, `.vault-meta/`, caches, build output, and unreviewed `dist/` archives.
- Third-party content whose license or permission is unclear.

## Public release checklist

1. Run the focused tests and complete pipeline.
2. Run both vault linters, deterministic hash verification, and Brainstein audit.
3. Scan tracked files and the final archive for secrets and local paths.
4. Confirm every raw capture is public, allowlisted, manifested, and licensed.
5. Confirm `LICENSE`, `THIRD_PARTY_NOTICES.md`, and the upstream license copy are present.
6. Inspect the final archive entry list for runtime artifacts, symlinks, and unsafe paths.
7. Verify repository visibility, Actions permissions, branch rules, and security settings.
8. Record checks that did not run and preserve the explicit runtime evidence limits.

The generated `dist/` archives are local verification artifacts and are not
committed. Publishing a GitHub release or changing repository visibility requires
a separate reviewed decision.

The hosted documentation site is outside the 0.2.0 release. The
tracked README, guide, diagrams, and image provenance are its public-facing
documentation surfaces.
