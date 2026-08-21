# DeepSeek Harness Brain Research Plan

Status: official-source baseline complete at the pinned commit. The current
research pack is sufficient for domain-adapted internal use, not for the
60-citation Brainstein market-research threshold or market readiness.

## Source Targets

- Official product, platform, API, or vendor docs for DeepSeek Harness architecture, operations, extension development, security, testing, and debugging.
- Primary datasets or exports the buyer already controls.
- Standards-body, regulator, tax authority, accounting authority, legal, medical, security, or compliance sources when relevant.
- Dated practitioner sources only as supporting evidence.
- Market evidence: buyer pain, screenshots, communities, search demand, competitor products, and sales objections.

## Buyer Questions

- Who pays for this brain?
- What raw materials do they already have?
- What output saves time or reduces risk?
- What weekly or monthly workflow brings them back?
- What should the brain refuse to do?

## Official-Source Checklist

- [x] Source URL recorded.
- [x] Retrieval date recorded.
- [x] Version or commit recorded when available.
- [x] Developer-preview and compatibility limits recorded.
- [x] Confidence level assigned.
- [x] Contradictions and gaps recorded.

## Market Evidence Checklist

- [ ] Buyer role and budget evidence.
- [ ] Recurring workflow evidence.
- [ ] Existing messy raw-source evidence.
- [ ] Deliverable examples or screenshot-worthy outputs.
- [ ] Competitor/template/license review.

## Safety Questions

- Developer-preview churn makes package names, defaults, events, and on-disk formats stale quickly
- Everything-is-a-plugin flexibility can hide load-order, ownership, disposal, and cross-capability integration failures
- A green unit suite can miss broken Loader composition, built entrypoints, browser output, or real-provider behavior
- Permission, sandbox, approval, filesystem, subprocess, and credential layers can be confused as one control even though they are separate
- Generated catalogs and bilingual derivatives may drift if hand-edited instead of regenerated through repository gates
- Local build artifacts may be mistaken for tracked source or current release evidence

## Adapter Requirements

- Define raw input types and schemas.
- Define importer behavior and source manifest fields.
- Define synthesis rules that separate facts, interpretation, and recommendations.
- Define report sections and required citations.
- Define refusal rules, approval state, and rollback fields.
- Add fixtures and tests for every supported input type.

## Freshness Requirement

Refresh official primary sources at each upstream release and before any
external release. Do not inflate the current official repository pack into a
market-demand research pack.
