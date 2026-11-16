# React performance decisions

Adapted from Vercel's performance priorities; apply against an observed bottleneck or the requested feature.

- Start independent data reads together; preserve dependencies and permission checks. Place waits near consumers and use loading boundaries where partial content is useful.
- Keep server-only dependencies out of client imports. Inspect bundle evidence before changing import paths; only use package-supported entrypoints. Defer expensive optional UI when doing so preserves interaction and accessibility.
- Transfer only the data client components need. Do not hold user-specific request state in shared module variables. Authenticate mutations independently of their UI entry point.
- Reuse the existing client data layer for deduplication and invalidation. Define stale, loading, retry, and mutation behavior before adding another cache.
- Derive inexpensive values during rendering. Put user-triggered work in handlers. Profile costly updates before adding memoization or broad context providers.
- Validate behavior and compare comparable measurements; a smaller patch or extra memo does not itself demonstrate better performance.

Official rule details: [Vercel React best practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices).
