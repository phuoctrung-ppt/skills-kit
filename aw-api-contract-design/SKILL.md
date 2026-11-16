---
name: aw-api-contract-design
description: Design versioned API or event contracts, errors, fixtures, and compatibility rules from accepted semantics; do not invent unapproved product behavior.
---

# API Contract Design

## Trigger and inputs
Use when consumers and providers need a new or changed interface. Require accepted domain rules, use cases, non-functional requirements, ownership, authentication semantics, and relevant data or architecture constraints.

## Output and scope
Produce a versioned contract defining requests, responses or events, validation, errors, authorization expectations, idempotency, pagination where relevant, compatibility classification, and representative fixtures. Do not silently change product meaning or provider internals.

Use [api-handoff.md](templates/api-handoff.md) to bind schema, fixtures, recipients and observed conformance to one revision.

## Method
1. Map operations to acceptance criteria and domain invariants.
2. Specify success and failure semantics before representation details.
3. Make optionality, defaults, identifiers, ordering, and retry behavior explicit.
4. Assess consumer impact and versioning for every breaking candidate.
5. Validate fixtures against the contract and review the same revision with consumers and providers.

## Evidence, exit, and handoff
Exit when accountable reviewers accept one pinned revision and fixtures are valid. Hand it to frontend, backend, data, and QA owners. Contract changes require impact analysis and new acceptance; stale consumers return to their owners instead of being treated as compatible.
