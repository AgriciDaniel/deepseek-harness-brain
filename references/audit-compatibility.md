# Audit Compatibility Notes

As of 2026-08-21, Brainstein 1.2.0 category C8.3 checks only a repository-root
`wiki/sources` path, while this product correctly treats
`assets/template-brain/wiki/sources` and `examples/sample-vault/wiki/sources`
as vault roots. Other Brainstein checks already inspect those vault surfaces.

This path mismatch does not erase the substantive open requirement. C8.3 also
expects a research pack containing at least 60 dated URL citations, while this
brain deliberately carries a smaller official source pack focused on the pinned
Harness repository. The product does not add a duplicate root vault or symlink
to game the check. The finding remains open until a genuine market research pack
exists or the upstream checker accepts configured vault roots.

Local maturity is determined by executed adapter tests, strict vault lint,
sample regeneration, the committed tree hash, and the explicit release status.
It is not promoted by prose or empty adapter paths.
