---
name: aw-debugging-and-root-cause
description: Reproduce unexpected behavior, test hypotheses, identify the causal mechanism, and protect it with regression evidence; do not patch from intuition alone.
---

# Debugging and Root Cause

## Trigger and inputs
Use for defects, test failures, incidents, flaky behavior, or unexpected integration results. Require observed symptoms, environment and revision, available logs, recent changes, and a bounded scope.

## Output and scope
Produce a reproduction, ranked hypotheses, experiments, root-cause statement with confidence, fix or routing recommendation, and regression coverage. Do not expand into unrelated cleanup or claim cause from correlation.

## Method
1. Reproduce the smallest failing case and preserve the original signal.
2. Separate facts from hypotheses and vary one causal factor at a time.
3. Trace data and control flow across the failing boundary.
4. Confirm the mechanism by removing or controlling the cause.
5. Add a failing regression before the fix when implementation is authorized.

## Evidence, exit, and handoff
Record revision, environment, reproduction steps, experiments, outputs, and remaining uncertainty. Exit when the cause is confirmed or a blocker has an owner and resume condition. Hand the fix task to the owning engineer and incident implications to reliability/release owners.
