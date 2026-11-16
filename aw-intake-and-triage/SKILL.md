---
name: aw-intake-and-triage
description: Frame a requested change, its risk, baseline, and routing before work is planned; do not use to design or implement the solution.
---

# Intake and Triage

## Trigger and inputs
Use for a new change, incident follow-up, or materially changed request. Require the stated goal, known constraints, repository or system context, and current authorization. Ask only for missing facts that alter routing or risk.

## Output and scope
Produce a change brief with type, outcome, affected systems, exclusions, baseline, risk profile, candidate owners, and open decisions. This skill classifies work; it does not grant access, approve product intent, or create implementation detail.

## Method
1. Restate the observable outcome and identify the decision owner.
2. Classify the change as feature, bugfix, refactor, hotfix, docs/config, spike, release, or incident work.
3. Identify affected boundaries, irreversible effects, sensitive data, and external mutations.
4. Select required discovery, design, contract, implementation, review, and release capabilities.
5. Record assumptions separately from evidence and route unresolved decisions.

## Evidence, exit, and handoff
Exit when the brief is specific enough to begin discovery or requirements work, with risks and missing authority visible. Cite request text and observed baseline facts. Hand the brief to the orchestrator and product analyst; send urgent operational risk to the reliability or release owner.
