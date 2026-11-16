# Request and capture review scope

Use the [request template](../templates/review-request.md). Supply actual task scope,
accepted input pins, output identity, files and evidence. The latest commit may be
unrelated to the task; choose the base from task/branch history, not `HEAD~1` by default.

When Git is available, inspect read-only status first (`git status --short`). For a
chosen committed base, inspect committed changes, `git diff --cached` and `git diff`
as applicable. Enumerate new untracked files with `git ls-files --others --exclude-standard`
and inspect their relevant contents; normal diffs omit them. Include deletions, renames,
binary/generated deliverables and file modes when they affect behavior. Separate
pre-existing user changes from task output instead of silently including or discarding them.

A commit SHA identifies committed files only. For dirty work, attach a stable snapshot
or manifest of relevant path/content digests alongside the diff; record the base and
capture time. If files change during review, recapture/recheck affected scope.
Never run `git add`, commit, stash or reset merely to manufacture a review snapshot.

Without Git, provide explicit old/new files or a reproducible path/digest snapshot and
declare what historical comparison is unavailable. No files supplied means review pending,
not “no findings”. Inspect for secrets before sharing evidence; do not dump unrelated
untracked/private files into the packet.

If native subagents are unavailable, hand the same packet to an eligible human or separate
reviewer session. The author may prepare a labelled self-review but cannot certify it as independent.
