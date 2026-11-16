---
name: aw-frontend-implementation
description: Implement accepted interface behavior and API consumption within assigned frontend paths; do not invent missing product design or contract semantics.
---

# Frontend Implementation

## Trigger and inputs
Use when frontend work has accepted requirements, an accepted design revision where applicable, a pinned API contract where applicable, allowed paths, and test expectations. Design N/A needs a reason such as a refactor that does not change user-facing behavior. API N/A separately records that the task has no API boundary. A local-only UI can still require design. Missing product-facing states return to the designer; continue independent preparation within scope.

## Output and scope
Produce frontend code, component or interaction tests, accessibility/performance considerations, and a handoff. Internal component structure and state management are engineering choices inside scope; design, domain rules, and shared contracts remain owned elsewhere.

## Method
1. Map acceptance criteria to visible states and interactions.
2. Follow repository conventions and existing tokens/components.
3. Implement semantic structure, keyboard/focus behavior, responsive states, errors, and loading.
4. Use contract-derived fixtures for isolated work and label them as doubles.
5. Apply TDD and verify relevant client boundaries before handoff.

## Evidence, exit, and handoff
Provide requirement/design/API revisions, changed paths, test results, and screenshots or render evidence only when they prove relevant behavior. Exit when assigned states work and integration needs are explicit. Hand to reviewer and integrator; raise design or contract changes to their owners.
