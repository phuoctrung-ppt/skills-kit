---
name: aw-backend-implementation
description: Implement domain and server behavior against accepted contracts and data constraints within assigned backend paths; do not silently change public interfaces.
---

# Backend Implementation

## Trigger and inputs
Use with accepted criteria, a pinned API contract, domain/data constraints, authentication and error semantics, allowed paths, and test expectations. Missing semantics return to the appropriate owner.

## Output and scope
Produce backend code, domain/service tests, provider conformance, configuration notes, and a handoff. Own implementation internals in scope; do not redefine UI, product rules, shared schemas, or environment authority.

## Method
1. Map contract operations to domain invariants and authorization checks.
2. Validate untrusted input at boundaries and preserve defined error semantics.
3. Apply TDD to success, failure, retry, and concurrency risks as applicable.
4. Keep persistence and external-service effects explicit and recoverable.
5. Run provider conformance and affected integration tests.

## Evidence, exit, and handoff
Provide pinned revisions, changed paths, RED/GREEN/REFACTOR evidence, conformance results, and operational impacts. Exit when assigned behavior conforms to the accepted contract. Hand to reviewer/integrator; request a new contract revision for required public changes.
