---
name: aw-architecture-and-adr
description: Decide technical boundaries and consequential trade-offs with an architecture decision record; do not replace product requirements or routine local design.
---

# Architecture and ADR

## Trigger and inputs
Use for durable boundary, dependency, storage, integration, security, reliability, or deployment decisions with meaningful alternatives. Require accepted requirements, repository map, constraints, and relevant design/API/data context.

## Output and scope
Produce an ADR with context, forces, considered options, decision, consequences, compatibility, risks, and follow-up work. Avoid ADRs for reversible local implementation choices.

## Method
1. State the decision and quality attributes it must satisfy.
2. Verify current architecture and constraints from evidence.
3. Compare viable options against explicit criteria.
4. Define boundaries, ownership, failure modes, migration impact, and rollback implications.
5. Record dissent or uncertainty and the condition for revisiting the decision.

## Evidence, exit, and handoff
Exit after the accountable technical reviewer accepts a specific ADR revision. Cite measurements, repository evidence, and authoritative constraints. Hand constraints to API, data, implementation, QA, and release owners; escalate product trade-offs to the product decision owner.
