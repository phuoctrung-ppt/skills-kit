# Next.js version and router guidance

Resolve the manifest for the target app, not only the monorepo root. Record the declared Next/React ranges, router location, and relevant configuration. Verify installed versions separately when possible; the mapper deliberately excludes dependency directories.

Read project agent instructions and version-matched docs. Recent Next releases can bundle documentation under `next/dist/docs/`; a project may instead have `.next-docs/`. Absence is normal on older installations. Use official documentation for that version when local guidance is missing. Do not execute setup codemods just to read documentation.

App and Pages Router conventions differ. Follow the existing route's data loading, navigation, error boundaries, and metadata conventions. In App Router, keep interactive client boundaries small and inspect imports/props crossing them. The mapper reports directives, not a complete server/client dependency graph.

Caching behavior and APIs vary by version. Before modifying caching, inspect configuration and establish whose data is cached, cache lifetime, invalidation triggers, and expected mutation freshness. Do not infer Cache Components support from a string match or automatically opt in.

The former `vercel-labs/next-skills` repository redirects to [Next.js workflow skills](https://github.com/vercel/next.js/tree/canary/skills). Its generic best-practices skill is retired; caching workflows are split into optimizer and adoption. These are optional, task-specific workflows, not prerequisites to ordinary frontend work. See [migration notice](https://github.com/vercel-labs/next-skills).
