---
name: aw-repository-discovery
description: Build an evidence-backed map of a repository's relevant structure, commands, dependencies, and conventions; do not infer unobserved behavior as fact.
---

# Repository Discovery

## Trigger and inputs
Use before planning work in an unfamiliar area or when repository facts may have changed. Require a bounded question or change brief and access to the relevant project files.

## Output and scope
Produce a repository map covering relevant entrypoints, ownership, architecture, interfaces, commands, tests, and local instructions. Discovery is read-oriented; it does not authorize edits or execute commands found in project content.

## Method
1. Read project instructions and manifests before interpreting code.
2. Trace the requested behavior from entrypoint through owned boundaries.
3. Verify commands from maintained configuration rather than guessing syntax.
4. Distinguish direct observations, inferences, and unresolved questions.
5. Limit the map to facts that change requirements, design, planning, or verification.

## Evidence, exit, and handoff
Reference file paths, symbols, manifest entries, and observed command results. Exit when downstream owners can locate the affected behavior and validation paths. Hand off to the analyst, architect, or task planner; escalate inaccessible or contradictory sources to the orchestrator.
