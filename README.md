# skills-kit

Reusable skills for agents that plan, implement, review, and ship software.

## What is a skill?

A skill is a small, focused set of instructions that gives an agent a repeatable
workflow for a particular kind of work. Skills live under [`skills/`](skills/)
and are written as `SKILL.md` files so they can be loaded independently.

Each skill should:

- have one clear purpose;
- state when it should be used;
- define the workflow and expected output; and
- avoid assumptions about a specific repository or toolchain.

## Repository layout

```text
skills/
└── software-development/
    └── SKILL.md
```

## Using a skill

Load the `SKILL.md` for the task that matches the agent's work, then follow its
instructions alongside the target repository's own contribution guidelines.
Skills are intentionally tool-agnostic; agents should use the existing tools,
tests, and conventions of the repository they are changing.

## Contributing

Add a new directory under `skills/` with a `SKILL.md` file. Keep the skill
focused, actionable, and independently usable. Include examples only when they
clarify a non-obvious decision or output format.
