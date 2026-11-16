# Domain extraction contract

`scripts/map-domain.py` uses Python 3 standard library. Supply one of `--task` or `--task-file`, plus an existing `--root` directory. JSON is printed to stdout; redirect only to a user-appropriate artifact location. The script never edits the repository or fetches external data.

- `deliverables`: keyword-based artifact routing, with matching terms and local reference paths.
- `domain_candidates`: hypotheses from task and repository evidence; overlapping domains are allowed. No numeric confidence pretending to be a probability.
- `entities`, `roles`, `constraints`: candidate symbols or explicitly labelled statements with file/line evidence; not a complete domain model.
- `token_sources`: CSS custom-property names or token-like JSON paths. CSS selector semantics and token alias validity are not parsed.
- `task_files`: lexical matches to task terms; inspect these files before using them.
- `knowledge`: task-routed CSV lookup results, separate from repository evidence; see [csv-knowledge.md](csv-knowledge.md).
- `scan`: files read, skipped/limited counts, and limitations.

The scanner excludes hidden paths, common dependencies/build output, skill/plan/workflow folders, agent instruction files, symlinks, lockfiles, and secret-like filenames. It does not parse gitignore; use a narrow root if ignored application text must be excluded. Only known text extensions are read, at most 500 files and 128 KiB per file. Each result collection is bounded and reports omitted entries.

Matches are lexical, not AST or semantic analysis. A field called `User` does not establish a persona. A README example does not establish a production feature. Task negation and multilingual meaning require agent interpretation. Domain labels are search hints, not recommendations or inferred business rules. Empty results mean insufficient evidence, not absence of a feature.

Task classification supports finite Vietnamese aliases; matched terms may be normalized English terms. `knowledge.normalized_task` records the normalized query. `--query` changes CSV retrieval only. Missing datasets are explicit `error` results, not invented defaults.
