---
name: aw-test-strategy
description: Design risk-based test coverage and acceptance scenarios across appropriate levels; do not postpone all quality work until implementation ends.
---

# Test Strategy

## Trigger and inputs
Use while requirements and contracts are being finalized or when change risk needs explicit coverage. Require acceptance criteria, design/API/data/architecture revisions, risk profile, supported environments, and known failure history.

## Output and scope
Produce a traceable strategy covering scenarios, levels, environments, test data, oracles, specialty checks, ownership, and exit criteria. QA strategy complements rather than replaces implementer unit and component tests.

## Method
1. Rank behaviors and boundaries by impact and likelihood.
2. Assign the lowest meaningful test level to each risk, adding real integration where boundaries matter.
3. Cover success, validation, authorization, failure, retry, concurrency, recovery, and compatibility as applicable.
4. Define reproducible data and environment prerequisites.
5. Identify acceptance blockers, exploratory charters, and evidence retention.

## Evidence, exit, and handoff
Exit when every applicable acceptance criterion has an owner and verification path without wasteful duplication. Hand scenarios to implementers and the integration plan to QA/integrator. Route untestable requirements or unavailable environments to their owners instead of lowering criteria silently.
