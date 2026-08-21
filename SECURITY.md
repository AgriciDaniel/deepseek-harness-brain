# Security Policy

## Current security status

DeepSeek Harness Brain is an advisory research artifact. It has automated secret,
path, archive, provenance, and vault-integrity checks, but it has not received a
comprehensive independent security audit. A passing scan is release hygiene, not
proof that the software or upstream DeepSeek Harness is secure.

## Supported versions

| Version | Supported |
|---|---|
| 0.2.x | Yes |
| Earlier versions | No |

## Reporting a vulnerability

Do not open a public issue containing a vulnerability, credential, token, private
client data, raw client capture, or local filesystem path.

Use GitHub's private vulnerability reporting for this repository when it is
available:

`https://github.com/AgriciDaniel/deepseek-harness-brain/security/advisories/new`

If that route is unavailable while the repository is private, contact the owner
through an existing private channel. Include only sanitized reproduction steps,
the affected commit or version, expected impact, and whether the issue concerns
the importer, vault generation, packaging, or agent permissions.

This is a volunteer project with no response-time guarantee. The maintainer will
try to acknowledge a valid report, assess impact, prepare a fix, and coordinate
disclosure before public detail is shared.

## Scope

In scope:

- Secret or private-path leakage from generated vaults or packages.
- Importer path traversal, unsafe symlink handling, or unexpected file reads.
- Archive traversal, unsafe entries, or missing release exclusions.
- Agent permissions that exceed the documented advisory boundary.
- Integrity or provenance checks that can be bypassed.

Out of scope:

- Vulnerabilities in upstream DeepSeek Harness itself. Report those to the
  upstream project through its official security channel.
- Findings that require publishing real credentials or private data.
- General support, architectural disagreement, or unsourced speculation.

## Secret handling

- Never commit `.env` files, keys, tokens, credentials, cookies, or private vaults.
- Use obvious placeholders in examples.
- Rotate a real credential immediately if it ever enters Git history. Deleting
  the visible file is not enough.
- Treat generated archives as untrusted until their contents and checksums pass.
