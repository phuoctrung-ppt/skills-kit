---
name: aw-skill-evaluation-and-maintenance
description: Evaluate and revise workflow skills using realistic routing, scope, outcome, and regression scenarios; do not infer model or harness success from source text alone.
---

# Skill Evaluation and Maintenance

## Trigger and inputs
Use for a new or changed skill, a confirmed workflow failure, compatibility claim, or versioned catalog release. Require the skill revision, intended triggers and boundaries, representative tasks, baseline where available, harness metadata, and release policy.

## Output and scope
Produce behavioral scenarios, deterministic validation, observed results, analysis, focused revisions, compatibility labels, and migration notes. Do not auto-release shared skills from one project task or fabricate unrun evaluations.

## Method
1. Test positive trigger, negative trigger, missing input, scope violation, stale artifact, unavailable tool, and ordinary-task behavior as applicable.
2. Judge actual decisions, artifacts, evidence, and handoff usability with an independent rubric.
3. Separate schema/fixture validation from model and native harness execution.
4. Reproduce confirmed failures before changing instructions; make the narrowest useful correction.
5. Rerun relevant regression scenarios and version material behavior changes.

## Evidence, exit, and handoff
Record skill and harness versions, scenario inputs, outputs, rubric decisions, repetition, and limitations. Exit when required deterministic checks pass and behavioral claims match observed evidence. Hand release candidates to an independent reviewer/workflow maintainer; unresolved regressions block only the claims or release gates they affect.
