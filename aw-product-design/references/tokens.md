# Design tokens

Inspect reported token sources before adding definitions. CSS variables, Tailwind theme entries, token JSON, component variants, and design-tool variables may all participate; the mapper's CSS/JSON scan is only a starting point.

Use the project's existing format. For a new token set, choose a small machine-readable JSON or CSS representation suitable for the target tool. Separate:

- Primitives: raw palette, spacing, type sizes, radii, duration.
- Semantics: surface, text, border, action, feedback, focus roles.
- Component roles: tokens only where a component needs a distinct contract.

Example mapping: `palette.brand.600 → color.action.primary → button.primary.background`. Every proposed token should have a real use in the requested screens. Avoid a full speculative palette or component library.

Preserve alias relationships across themes. In CSS, use `--button-primary-bg: var(--color-action-primary)` rather than baking the current light-theme value into the component. Define aliases in the same theme scope as their semantic targets when necessary; custom-property aliases resolved on an ancestor do not automatically re-resolve against a descendant's override.

For a JSON alias graph, verify missing references, cycles, type/unit compatibility, and complete semantic coverage for each requested theme. Do not present a regex inventory as a token validator. Keep existing token names unless a migration is authorized; record old-to-new names if renaming is required.

Deliver the token artifact and a short usage mapping with name, role, value/alias, theme, and consuming component. Check text and interactive-state contrast on the actual surface. Include typography line height, visible focus, and reduced-motion behavior where the design uses them. Native Figma variables require actual Figma tooling and binding verification.
