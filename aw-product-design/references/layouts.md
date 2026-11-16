# Sketches and wireframes

Start from the actor's goal, entry point, and successful outcome. Reuse actual domain nouns and sample content from the brief. Preserve uncertainty where requirements are absent.

For a sketch, focus on navigation, content grouping, hierarchy, and the main action. Show alternate layouts only when a real decision needs comparing. Annotate why the arrangement supports the user's task. A sketch may be ASCII or a local vector/HTML artifact; do not inflate it into production code.

For a wireframe, assign stable screen IDs and map each screen to:

| Item | What to specify |
| --- | --- |
| Entry and exit | Trigger, destination, back/cancel behavior |
| Content | Domain object, essential fields, representative lengths |
| Actions | Primary action, supporting actions, availability rules |
| States | Applicable initial, loading, empty, success, invalid, failure, forbidden states |
| Layout | Reading order, grouping, narrow-screen reflow, sticky regions if needed |
| Accessibility | Headings, labels, focus destination after navigation/dialog actions |

Include only states supported by the requested flow. A booking flow may need unavailable-slot and confirmation screens; do not invent cancellation charges or clinical advice from a fitness keyword.

Reuse existing navigation and patterns before proposing alternatives. Keep visual fidelity low until information structure is reviewable. Link uncertain rules to questions rather than silently filling them in.

Handoff should make `screen → domain object → action → next state` inspectable. For layout-only work, a concise annotated artifact and state table can be sufficient.
