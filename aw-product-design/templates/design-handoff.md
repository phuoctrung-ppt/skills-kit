# Design handoff

Copy this template into a project-owned artifact. Replace instructions with actual
facts; use `unknown — owner — resume condition` for gaps. No default approval.

## Identity and inputs
- Artifact ID / revision / status (draft, in-review, accepted):
- Designer / recipient (FE and QA) / assigned scope:
- Requirements IDs and pinned revisions; applicable API/ADR revisions:
- Deliverable: exploratory sketch, wireframe, tokens or prototype:
- Design files / launch instructions if needed:
- Existing branding, components, tokens and target form factors:

## Screens and transitions
| Criterion | Screen/state ID | Content and actions | Trigger / guard | Destination / feedback | Keyboard / focus |
|---|---|---|---|---|---|
| Fill with actual criterion | | | | | |

Cover applicable initial, loading, empty, invalid, forbidden, error, retry and success
states. Explain N/A based on the actual flow. Name back/cancel/close behavior without
inventing business cancellation policy. Identify which decisions are proposals.

## Responsive and tokens
| Screen/component | Narrow / wide behavior | Token or primitive | Content boundary / accessibility intent |
|---|---|---|---|
| | | | |

Reuse real token names; unknown brand details stay unresolved. Include long/empty
content behavior, semantics, labels, announcements and reduced-motion intent as relevant.

## Checks and gaps
| Check | Artifact revision | Environment/tool or procedure | Actual outcome / evidence | Remaining owner |
|---|---|---|---|---|
| Render / interaction / keyboard / contrast as applicable | | | not run until observed | |

Prototype fixtures simulate behavior; record whether persistence/backend integration
exists. No render tool means visual verification not run, not a visual pass.

## Recipient decision
- Open decision, impact, owner and concrete resume condition:
- FE engineering freedom: component boundaries/state internals inside accepted design.
- Applicable design decisions still missing: affected FE work remains blocked.
- Reviewer identity / exact output revision / decision / timestamp / findings:
- A revised design requires affected FE/QA input pins and evidence to be refreshed.
