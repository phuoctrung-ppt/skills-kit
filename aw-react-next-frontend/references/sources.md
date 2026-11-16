# Sources and scope

This is a custom local adaptation with an original repository mapper. It does not install or reproduce the complete upstream skills. No upstream command is run by the mapper.

Bundled community CSV data comes from [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/src/ui-ux-pro-max/data). See [csv-knowledge.md](csv-knowledge.md) and the bundled provenance manifest/license. CSV recommendations are secondary to official framework guidance below; embedded version claims are upstream metadata, not locally verified compatibility.

- [Vercel React and Next.js skill catalog](https://vercel.com/docs/agent-resources/skills#react-and-next.js): selection starting point.
- [React performance skill](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) and [upstream source](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices): performance priorities.
- [Composition skill](https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns) and [upstream source](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns): component API and state ownership guidance.
- [Next skill migration notice](https://github.com/vercel-labs/next-skills) and [current workflow source](https://github.com/vercel/next.js/tree/canary/skills): version-aware routing. The catalog still lists older names; use maintained source guidance when they disagree.

React Native, framework migrations, deployment, and monorepo infrastructure are outside this skill's default scope. Official upstream installation is a separate choice; this skill operates offline using its included references and local evidence.
