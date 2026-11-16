# Receive and resolve findings

Read each finding, locate the cited behavior and verify its premise against the
accepted specification and actual target version. A confident review is not proof.
Reproduce meaningful defects before fixing; distinguish behavioral failure from setup failure.

Record disposition per finding: confirmed, needs clarification, disproved with evidence,
or accepted risk by its authorized owner. Clarify uncertain items and continue unrelated
work whose scope and dependencies are clear. Do not treat review suggestions as permission
to add unrelated features, redesign contracts or mutate environments.

Prioritize blockers by actual impact. Fix within assigned ownership, add the meaningful
regression, run affected verification and return the new output revision with evidence.
Explain technical disagreement with the relevant invariant/version/result; revise your
conclusion when new evidence contradicts it. Avoid replacing a review response with generic praise.

The independent recipient decides whether the revised output meets acceptance. Record
unresolved findings and their owner; do not silently close them because other tests pass.
