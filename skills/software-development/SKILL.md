---
name: software-development
description: A disciplined workflow for making small, tested, and reviewable changes to a software repository.
---

# Software development

Use this skill when an agent must change code in an existing repository.

## Workflow

1. Inspect the repository, its contribution instructions, and the history
   around the affected code before editing.
2. Restate the requested behavior and identify the smallest complete change.
3. Find the existing test, lint, and build commands. Prefer focused checks for
   the files being changed.
4. Make a surgical implementation that follows local conventions. Do not
   rewrite unrelated code or introduce a new dependency without a clear need.
5. Add or update focused tests for the changed behavior when test infrastructure
   exists.
6. Run the focused checks, then manually review the diff for accidental
   changes, insecure inputs, and missing error handling.
7. Summarize the implementation, validation performed, and any remaining
   limitations.

## Completion criteria

A change is ready when:

- the requested behavior is implemented;
- existing behavior remains intact;
- relevant tests and checks pass;
- no secrets or generated artifacts were added; and
- the diff is limited to the requested work.
