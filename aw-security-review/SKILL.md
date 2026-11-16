---
name: aw-security-review
description: Use when a scoped change affects trust boundaries, authorization, authentication, untrusted input, sensitive data or secrets, or when a security review is requested.
---

# Security Review

Identify the affected revision, assets, actors, trust boundary, deployment context and
approved policy. Discover policy in project-owned documents; do not assume an AGENTS
section, role list, tenancy model, compliance regime or native command exists.

Produce a scoped report: abuse cases, controls, reproducible findings, impact/likelihood,
evidence and residual risk. Use [security-review.md](templates/security-review.md).
Unknown authorization semantics require a policy owner; prepare conditional tests while
that decision is pending. A checklist tick or missing test is not proof of a vulnerability.

## Load only relevant guidance
- Access to resources, tenants or privileged actions: [authorization.md](references/authorization.md).
- Login, credentials and session lifecycle: [authentication.md](references/authentication.md).
- Secrets, logs, rotation and recovery: [secrets-management.md](references/secrets-management.md).
- Changed input/output, dependency and external-effect boundaries: [boundary-review.md](references/boundary-review.md).

Use existing framework controls and version-matched official guidance; do not introduce
a new auth library, token policy or architecture merely to match an example. Security
review is read-oriented. Implementers apply relevant controls within assigned paths;
the reviewer reports findings, and the authorized owner accepts residual risk.

Test with synthetic data in authorized isolated environments. Record actual results,
not-run checks and reproduction requirements without exposing secrets. Fixes return to
their owning task and require retesting at the new output revision. Material adjacent
risks have a named owner; they do not silently expand this task into a platform rewrite.
