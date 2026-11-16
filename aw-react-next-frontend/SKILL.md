---
name: aw-react-next-frontend
description: Implement, refactor, and review React or Next.js web interfaces using task-specific repository mapping and Vercel performance and composition guidance. Use for components, routes, data flows, and frontend performance; visual exploration without implementation belongs to a design workflow.
---
# React and Next.js Frontend

Connect the requested user journey to existing code before choosing implementation patterns. Preserve the project's framework, router, component library, and contracts.

## Map the task

Run this read-only mapper, substituting the skill's actual directory:

```bash
python3 /path/to/react-next-frontend/scripts/map-task.py --root /path/to/project --task 'Add booking filters with URL state and loading feedback'
```

The JSON reports declared dependency ranges per manifest, route candidates, reusable UI/contracts/tokens, technical signals, task matches, guidance, and `knowledge` results from bundled CSV data. Each result carries its CSV path and record number. It runs offline with Python's standard library. See [mapping.md](references/mapping.md) for interpretation.

Use `--query 'data fetching cache'` when the task's technical intent is not recognized. Vietnamese aliases cover common tasks, not arbitrary translation. Read [csv-knowledge.md](references/csv-knowledge.md) for direct lookup, dataset scope, and source verification. Preserve the original user task when refining the search query.

Read the strongest task matches and their immediate callers. Turn the evidence into a compact mapping: user action → route/component → state/data contract → validation and visible feedback. A keyword hit is a candidate, not proof of domain behavior. When no matches exist, use the request and actual project structure; record missing contracts rather than inventing them.

## Choose only relevant guidance

- Components, fetching, bundle size, or rendering: [react-performance.md](references/react-performance.md).
- Shared components, variant APIs, provider/state ownership: [composition.md](references/composition.md).
- A Next.js app or explicitly requested Next implementation: [next-version-guidance.md](references/next-version-guidance.md). Verify the target app's version and router; sibling apps may differ.
- Provenance, official upstream choices, and migration status: [sources.md](references/sources.md).

For Next APIs, inspect installed/version-matched documentation when present, following project agent guidance. Otherwise consult official documentation matching the declared version, stating that a version range is not an installed version. Do not upgrade React/Next, install libraries, enable Cache Components, or migrate routers merely to follow a reference.

Treat CSV records as community suggestions; official Vercel/React/Next.js guidance and the existing project take precedence. Check each record's platform, `Applies To`, and documentation link before applying. Dependency evidence across a monorepo identifies candidates; choose the target app explicitly.

## Implement and verify

Before behavioral implementation, require accepted requirements, the applicable design revision and pinned API contract. If design or API is not applicable, record the reason in the task packet. Missing UX decisions go to the product designer; missing contract semantics go to the API owner. Do not silently create wireframes or redefine shared schemas. Component structure, state management, semantic HTML and performance remain frontend engineering decisions within the accepted design.

Keep writes within assigned frontend paths. Use RED/GREEN/REFACTOR for behavior changes and hand off input revisions, changed paths, criterion-to-test mapping, actual results and remaining integration needs to an independent recipient. Shared contract changes require a versioned handoff before FE/BE resume parallel work.

Use existing semantic tokens and primitives; map supplied design states to real loading, empty, error, success, disabled, and focus behavior as relevant. Keep API validation and authorization on the server; client checks serve usability. Distinguish prototype fixtures from live integration.

Keep changes proportional to the task. Use the project's available type/lint/build checks and behavior tests that exercise changed flows. For visible work, inspect supported viewport sizes and keyboard behavior when browser tooling is available; otherwise identify the unverified visual checks. Report changed behavior, evidence, and remaining limitations. Never claim a measured performance improvement without measurement.
