# Mapper output

`scripts/map-task.py --root DIRECTORY --task TEXT [--query ENGLISH_TERMS]` writes JSON to stdout. Invalid roots/arguments fail with a nonzero exit. The scan reads source/config files without network access, subprocesses, repository imports, or modifications.

- `manifests`: dependency sections with declared ranges per package.json, plus available script names; commands are never emitted or executed. These are declarations, not installed-version evidence.
- `routes`: file-convention candidates grouped by router and owning manifest. Confirm custom page extensions/configuration manually.
- `inventory`: candidate component, contract, and token files; token identifiers where recognizable.
- `signals`: lexical path/line evidence for directives, data hooks, fetching, caching, and rendering patterns. Comments/examples can cause false positives.
- `task_matches`: ranked path or identifier hits against meaningful task words, with matched terms and evidence lines. This is lexical domain mapping, not inferred business requirements.
- `guidance`: relevant included reference paths and selection reasons.
- `knowledge`: normalized task, extracted technical intent, actual lookup query, and per-domain CSV searches. Results include source path, one-based CSV record, score, matched terms, original values, and routing reason. `no_match` means no evidence; `error` means unavailable/invalid data. Neither justifies inventing recommendations.
- `warnings` and `scan`: scope and truncation details.

The scan ignores symlinks, hidden directories, common dependency/build folders, secret-like filenames, lockfiles, `skills`, `plans`, `workflow`, and agent instruction files. Design token files remain eligible; credential token filenames such as `access-token.json` do not. It handles common nested `.gitignore` patterns conservatively without invoking Git. Negation/escaped patterns and exact Git wildcard semantics are not fully implemented; warnings expose this limitation. Ignored parents stay excluded. It does not consult global Git excludes or `.git/info/exclude`.

Default caps: 4,000 visited file entries, 192 KiB per readable file, and 120 entries per output collection. Large, unreadable, binary, unsupported, or capped inputs produce counts/warnings. No source snippets or token values are printed, but paths, dependency declarations, and identifiers are still repository information. Treat output accordingly. Search deliberately within a narrower root when the scan is partial; manually inspect evidence before editing.

Run `python3 scripts/test-mapping.py` from this skill directory for the isolated behavioral fixture. The test creates and removes its own temporary workspace; it does not execute fixture package scripts.

Run `python3 scripts/test-csv-mapping.py` for real-data lookup, Vietnamese intent, source-record fidelity, unknown queries, framework routing, and missing-data behavior. See [csv-knowledge.md](csv-knowledge.md) for data use and limitations.
