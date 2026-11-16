# Data design / migration handoff

- Artifact ID/revision/status; data owner, backend/release recipients:
- Requirements, API, schema revisions; assigned paths and authorized environment:
- Current data shape/volume evidence; unknown data conditions:
- Target invariants, constraints, retention and access patterns:

| Step | Compatibility / locking impact | Execution prerequisite | Verification query/procedure | Recovery / interruption handling |
|---|---|---|---|---|
| Expand / backfill / verify / contract where applicable | | | | |

- Representative isolated data and actual test results:
- Query-plan/performance evidence when needed; no measured claim without measurement:
- Irreversible effects, backup/restore rehearsal, recovery owner:
- Exact output revision, recipient decision, timestamp, findings:

An accepted plan is not production execution authority. Record missing access or
data evidence with an owner and resume condition; never include credentials here.
