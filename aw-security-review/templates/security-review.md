# Scoped security review

- Task / reviewer / reviewed revision / paths / trust boundaries:
- Approved policy, contract, architecture revisions; data classification:
- Actors/assets/entrypoints; environment and permitted test actions:
- Unknown policy decisions / accountable owner / resume condition:

## Authorization / abuse cases
| Case | Actor / credential | Resource / tenant | Operation | Policy source | Expected result | Actual result / evidence |
|---|---|---|---|---|---|---|
| | | | | unknown until supplied | conditional / pending | not run |

Include relevant direct, alternate, bulk/export/download and revoked-membership paths.
Test identities/data are synthetic. Absence of live access is not an authorization pass.

## Findings and residual risk
| Finding | Location / revision | Impact / likelihood | Reproduction / evidence / assumptions | Fix owner / retest |
|---|---|---|---|---|
| | | | | |

- Checks executed and environment; supplied evidence inspected:
- Unrun checks and limitations; policy gaps distinct from confirmed vulnerabilities:
- Risk decision owner / decision / exact revision / timestamp, if actually made:
- Recipient and concrete next steps:

Never insert secrets or actual sensitive records in evidence. Reviewer findings do not
grant deployment authority or let the reviewer accept business risk for the user.
