---
name: aw-accessibility-verification
description: Verify keyboard, semantics, focus, contrast, motion, and assistive feedback against accepted interface behavior; do not redesign unrelated product flows.
---

# Accessibility Verification

## Trigger and inputs
Use for user-interface design or implementation and for regressions affecting interaction. Require acceptance criteria, design intent, target platforms, exact design/code revision, and a testable environment.

## Output and scope
Produce findings and evidence for semantic structure, keyboard operation, focus order/visibility, names and states, error feedback, contrast, zoom/reflow, motion, and assistive technology behavior as applicable.

## Method
1. Map critical journeys and states to accessibility expectations.
2. Inspect structure and programmatic relationships before visual polish.
3. Complete keyboard-only and focus testing across dynamic states.
4. Combine automated checks with manual inspection; automation is not complete coverage.
5. Propose fixes inside accepted behavior and route UX-changing decisions to design.

## Evidence, exit, and handoff
Record revision, platform/tool or manual procedure, reproduction, impact, and retest result. Exit when required journeys are operable or blockers have owners. Hand implementation findings to engineers and design conflicts to the product designer.
