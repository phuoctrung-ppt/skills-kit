# Interactive prototypes

Use the user's chosen platform; otherwise reuse the repository's stack. An isolated HTML/CSS/JS prototype is sufficient when no application exists and browser interactions are the deliverable. Do not install a framework merely to demonstrate navigation.

Define an interaction inventory before wiring screens:

`source screen/state | trigger | guard/validation | destination/state | focus behavior`

Connect the primary path and the relevant recovery path. Navigation, back, cancel, form validation, dialog dismissal, and reset should behave consistently. Use semantic controls, visible focus, keyboard interaction, and reduced-motion support. Dialogs should manage focus and restore it on close.

Keep fixture data visibly identified in the handoff. A simulated request must not imply a real booking, payment, account, or persistence operation. Do not call a live service merely to make a prototype seem realistic. If production integration is requested, map the actual contract and use the appropriate frontend/backend workflow.

Prefer representative domain content over placeholder slogans. Include long values and realistic empty/error states to expose layout problems. Match tokens and components to the existing system.

Verify links and interactive controls through the full flow, including refresh/reset expectations. Capture screenshots at meaningful widths when tooling is available. Report exactly which interactions were exercised and whether data survives reload. Deliver launch instructions only as needed to open the artifact.
