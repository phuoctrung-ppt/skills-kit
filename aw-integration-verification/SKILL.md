---
name: aw-integration-verification
description: Verify accepted components across real boundaries and pinned contracts; do not report contract-derived mocks as integrated behavior.
---

# Integration Verification

## Trigger and inputs
Use after component outputs are accepted and before integrated completion or release. Require exact output revisions, accepted contracts, environment prerequisites, integration scenarios, and accountable owners.

## Output and scope
Produce conformance, real-integration, and end-to-end results with requirement traceability and findings. This skill verifies combined behavior; it does not fix unowned components or waive unavailable environments.

## Method
1. Reject stale or mismatched artifact and contract revisions before testing.
2. Verify consumer and provider conformance independently where useful.
3. Run the real boundary for critical success and failure paths.
4. Distinguish environment, fixture, product, and implementation failures.
5. Retest affected paths after conflict resolution or component revision.

## Evidence, exit, and handoff
Record component/contract revisions, environment identity, scenario, result, and filtered logs. Exit when applicable acceptance paths pass on integrated outputs and blockers are resolved. Hand results to the integrator, reviewer, and release owner; route failures to the owning task.
