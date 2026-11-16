---
name: aw-test-driven-development
description: Implement observable behavior through RED, GREEN, and REFACTOR with reproducible evidence; do not count setup or import failures as RED.
---

# Test-Driven Development

## Trigger and inputs
Use for feature behavior, bug fixes, and behavior-preserving refactors that need characterization. Require an acceptance criterion or defect reproduction, owned scope, current contracts, and a runnable relevant test boundary.

## Output and scope
Produce focused tests, minimal implementation, refactoring, and evidence tied to one behavior. Do not alter product meaning, public contracts, or unowned paths to obtain a pass.

## Method
1. Select the smallest meaningful observable test.
2. RED: run it and confirm failure is caused by missing or wrong behavior.
3. GREEN: make the smallest coherent change and rerun the same test.
4. REFACTOR: improve structure, then rerun affected and boundary checks.
5. Inspect assertions so tests verify behavior rather than mirror implementation.

## Evidence, exit, and handoff
Record requirement, test identity, working directory or procedure, revisions, results, and relevant filtered logs. Exit after refactor checks pass and limitations are explicit. Hand code and evidence to the reviewer; report a blocked environment rather than fabricating results.
