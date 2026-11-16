---
name: aw-observability-and-incident-response
description: Define actionable service signals and manage incidents through evidence, safe mitigation, recovery, and learning; do not present hypotheses as proven causes.
---

# Observability and Incident Response

## Trigger and inputs
Use for operational readiness, service objectives, alerts, incidents, or post-incident learning. Require service boundaries, user outcomes, known dependencies, release context, available telemetry, and response authority.

## Output and scope
Produce signal requirements or an incident record with impact, timeline, observations, hypotheses, decisions, mitigation, recovery, owners, and follow-ups. Do not mutate environments or expose sensitive telemetry without authority.

## Method
1. Define meaningful indicators, objectives, alert conditions, and diagnostic context.
2. During an incident, stabilize user impact before deeper diagnosis when safe and authorized.
3. Preserve a factual timeline and label hypothesis confidence.
4. Verify recovery against user-visible and dependency signals.
5. Convert confirmed causes and response gaps into owned corrective work and tests.

## Evidence, exit, and handoff
Reference dashboards, queries, logs, release revisions, decisions, and recovery checks while filtering secrets and personal data. Exit when service is stable and follow-ups have owners. Hand product impact to stakeholders, defects to engineers, and release risks to the release owner.
