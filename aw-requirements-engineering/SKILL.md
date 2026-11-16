---
name: aw-requirements-engineering
description: Convert product intent into identified business rules, acceptance criteria, non-functional requirements, and exclusions; do not choose implementation design.
---

# Requirements Engineering

## Trigger and inputs
Use when desired behavior is ambiguous, new, or changing. Require the change brief, actors, known journeys, repository/domain evidence, constraints, and decision owners.

## Output and scope
Produce versioned requirements with stable IDs, rules, examples, measurable acceptance criteria, non-functional requirements, assumptions, exclusions, and trace links. Do not invent business policy, architecture, or visual layout.

Use the applicable sections of [requirements.md](templates/requirements.md) for a reusable handoff shape.

## Method
1. Model actors, goals, normal flow, alternate flow, and failures.
2. Resolve conflicting rules with the product decision owner.
3. Write criteria as observable outcomes, including error and retry behavior.
4. Record privacy, accessibility, performance, reliability, and compatibility needs when relevant.
5. Map each criterion to its source and mark unresolved decisions explicitly.

## Evidence, exit, and handoff
Exit when criteria are testable and owners have reviewed material product changes. Evidence includes source decisions and domain observations. Hand accepted requirements to design, architecture, API, data, and QA owners; return ambiguity to the product owner rather than hiding it in implementation.
