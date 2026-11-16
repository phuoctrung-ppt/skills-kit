---
name: aw-release-and-migration
description: Prepare and promote an accepted artifact with compatibility, migration, smoke, and recovery controls; do not deploy without explicit environment authority.
---

# Release and Migration

## Trigger and inputs
Use when accepted integrated output is being packaged, migrated, or promoted. Require release artifact digest, accepted verification, environment prerequisites, authority, configuration/data changes, rollout plan, and recovery objectives.

## Output and scope
Produce a release record containing artifact identity, compatibility, migration, rollout stages, smoke checks, observability, rollback/forward-recovery, approvals, and outcome. Role assignment alone is not deployment permission.

## Method
1. Verify exact artifacts and required acceptance records are current.
2. Rehearse migration and recovery proportional to risk.
3. Define staged rollout, health signals, stop conditions, and decision owners.
4. Execute only authorized environment actions and retain results.
5. Confirm smoke behavior and operational signals before completing promotion.

## Evidence, exit, and handoff
Record artifact/environment identity, authority, timestamps, migration and smoke results, and recovery readiness. Exit when the release outcome and follow-up are known. Hand operating context to reliability; on failure, stop at the defined condition and invoke the authorized recovery path.
