# Source selection

Reviewed 2026-10-12. These are source inspirations and optional deeper references, not installed upstream skills. Selected nextlevelbuilder CSVs are now bundled under `data/`. The instructions and mapper here are custom. Popularity on skills.sh informed discovery; fit to the requested artifacts informed selection.

| Source | Why selected | Custom addition |
| --- | --- | --- |
| [Anthropic frontend-design](https://skills.sh/anthropics/skills/frontend-design) · [upstream](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Domain-grounded visual direction, compact tokens, rough layouts | Explicit fidelity selection and evidence-backed handoff |
| [UI UX Pro Max](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) · [upstream](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Domain and stack search; product design research | Extract task and repository evidence before recommendations |
| [Design System](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/design-system) · [upstream](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/design-system/SKILL.md) | Token layers and component handoff | Focused token workflow without unrelated presentation modes |

Selected third-party CSV data is included with a pinned commit, checksum manifest, and MIT license. The BM25 retrieval helper is a custom implementation, not the upstream engine; a token compiler is not included. The local script extracts context; the agent makes design decisions and produces artifacts. For existing Figma work, use installed Figma workflows rather than reconstructing design-tool mechanics here.
