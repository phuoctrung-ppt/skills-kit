# Component composition decisions

For a component with conflicting mode flags, identify the actual user-facing variants before changing the API. Prefer explicit variant components or composable children when that makes invalid combinations harder to express. A simple boolean for one independent state may remain appropriate.

Use compound components when several parts share a coherent state model. Put ownership at their nearest useful provider; distinguish state, commands, and status so consumers need not know the storage mechanism. Avoid creating a provider solely to eliminate a short prop chain.

Preserve existing consumer behavior during refactors. Exercise representative combinations, controlled/uncontrolled usage where supported, focus movement, and labels. React 19-specific APIs require evidence that the target application supports them; do not rewrite React 18 refs or context based on newer examples.

Official rule details: [Vercel composition patterns](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns).
