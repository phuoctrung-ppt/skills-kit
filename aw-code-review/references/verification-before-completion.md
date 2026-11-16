# Verification evidence

Tie each claim to an observed check at the output revision being handed off. Read the
actual result and exit status; missing tools, timeouts or partial runs are limitations.
Do not rerun unrelated checks only to produce fresh-looking logs; rerun affected checks
after changes that invalidate their evidence.

| Claim | Evidence needed |
|---|---|
| Regression fixed | Reproduction failed for the intended behavior, then passed after fix |
| Build/typecheck/tests pass | Actual relevant command, environment, output revision and outcome |
| Requirements met | Criterion-to-behavior/evidence mapping and unresolved gaps |
| UI verified | Render/interaction procedure and observed results at relevant sizes/states |
| Integrated | Real consumer/provider or relevant system boundary exercised |
| Independently accepted | Eligible recipient decision for exact output revision |

Schema/link/package/helper checks verify those properties only. Planned checks, mock-only
results and model confidence cannot stand in for actual integration or visual evidence.
Retain concise logs or reproduction artifacts without secrets. A forwarded agent result
needs supporting evidence before you repeat its completion claim.
