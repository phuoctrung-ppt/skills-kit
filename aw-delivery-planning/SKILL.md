---
name: aw-delivery-planning
description: Turn accepted requirements and technical artifacts into dependency-aware vertical tasks with owners and readiness gates; do not dispatch work with missing mandatory inputs.
---

# Delivery Planning

## Trigger and inputs
Use after applicable requirements, design, architecture, API, data, and test strategy artifacts are accepted. Require their revisions, repository map, ownership boundaries, environment constraints, and risk profile.

## Output and scope
Produce a dependency graph and task packets containing goal, role, assignee, allowed and forbidden paths, inputs, outputs, scenarios, checks, reviewers, isolation, and escalation. Planning does not grant permissions or acceptance authority.

## Method
1. Slice work by user-visible or contract-observable outcomes.
2. Give shared artifacts and integration work explicit owners.
3. Pin dependency revisions and reject cycles or ambiguous scope overlap.
4. Mark gates required, satisfied, not applicable with reason, or waived by an authorized owner.
5. Dispatch only ready tasks; use sequential execution when isolation or safe parallelism is unavailable.

## Evidence, exit, and handoff
Exit when every task has a usable Definition of Ready and the graph has an integration path. Hand each packet to its worker and the graph to the orchestrator/integrator. Route missing product, design, contract, data, or authority inputs to their owners.
