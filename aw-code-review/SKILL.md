---
name: aw-code-review
description: Use when independently reviewing a scoped change, preparing a review handoff, responding to findings, or checking evidence before a completion claim.
---

# Code Review

Review specification conformance and correctness at an exact output revision.
Read the task packet, accepted inputs, repository standards and relevant code/tests.
Keep findings within scope; adjacent risks can be named with a separate owner.
Self-review is useful preparation but cannot satisfy independent acceptance.

## Select the needed reference
- Requesting review or capturing uncommitted work: [requesting-code-review.md](references/requesting-code-review.md), then [review-request.md](templates/review-request.md).
- Conducting review: inspect specification, risky paths, negative cases, ownership and evidence; use [review-report.md](templates/review-report.md).
- Receiving findings: [code-review-reception.md](references/code-review-reception.md).
- Reporting verification/completion: [verification-before-completion.md](references/verification-before-completion.md).

Read stack references only for the changed app/framework and task. A role or skill
does not grant write permissions. Review is read-oriented; fixes need assigned scope.
Choose an available independent reviewer through the harness, or a documented manual
handoff. No particular dispatch tool or Git history is required.

Each actionable finding identifies location, violated criterion/invariant, impact,
reproduction/evidence and expected correction. Distinguish blockers, suggestions and
unverified hypotheses. Recheck fixes at their new revision; prior approval does not
carry across changed output. Missing scope/code/policy prevents an acceptance claim,
while independent investigation can continue.
