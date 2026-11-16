---
name: aw-handoff-and-state-management
description: Package versioned work and evidence for recipient acceptance while preserving valid task-state transitions; do not self-accept or treat a summary as proof.
---

# Handoff and State Management

## Trigger and inputs
Use when work changes owner, enters review, becomes blocked, resumes, or is integrated. Require task identity, current state/revision, pinned inputs, produced outputs, evidence, scope, and named recipient.

## Output and scope
Produce a handoff with sender/recipient, attempts, revisions, behavior mapping, changed files, verification, compatibility, limitations, risks, rerun guidance, and recovery notes. Only the configured state owner updates canonical state.

Use [delivery-handoff.md](templates/delivery-handoff.md); fill only applicable sections and preserve not-run results honestly.

## Method
1. Confirm inputs are current and outputs identify exact revisions or digests.
2. Map requirements to changes and retained evidence.
3. Record RED/GREEN/REFACTOR or a justified not-applicable decision.
4. Separate verified results from claims, gaps, and blockers with owners.
5. Ask the recipient to accept or reject the exact output revision and record findings.

## Evidence, exit, and handoff
A handoff exits only when it is reproducible and the recipient decision is recorded. Broken links, stale inputs, unrun checks reported as passing, scope violations, or missing essential artifacts require rejection. Escalate blockers to the named owner with a concrete resume condition.
