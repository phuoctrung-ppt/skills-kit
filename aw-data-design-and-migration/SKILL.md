---
name: aw-data-design-and-migration
description: Design data models, migrations, integrity rules, query plans, and recovery evidence; do not run changes in environments without explicit authority.
---

# Data Design and Migration

## Trigger and inputs
Use for schema, stored-data meaning, migration, query, index, retention, or data-quality changes. Require accepted requirements/contracts, data ownership, current schema and volume evidence, compatibility window, and recovery objectives.

## Output and scope
Produce a data design or migration with invariants, compatibility, rollout phases, validation queries, performance impact, and rollback or forward-recovery guidance. Do not change product/API semantics or assume production access.

Use [data-handoff.md](templates/data-handoff.md) for execution prerequisites, verification and recovery ownership.

## Method
1. Inspect actual schema, constraints, access patterns, and representative scale.
2. Define target invariants and transformation rules, including null and invalid data.
3. Use expand/backfill/verify/contract phases when compatibility requires them.
4. Plan idempotence, batching, locking, observability, and interruption recovery.
5. Test on representative isolated data and review destructive or irreversible steps.

## Evidence, exit, and handoff
Record schema revisions, test data characteristics, dry-run or test results, query plans where relevant, and recovery rehearsal. Exit when owners can execute safely under granted authority. Hand to backend, QA, release, and reliability owners; escalate unknown data conditions before mutation.
