# Authorization and tenant boundaries

Read the approved actor/action/resource policy before assigning expected allow/deny
results. Authentication alone does not establish access. Recommend least privilege and
denial by default as control principles; missing project policy still leaves scenario
expectations conditional, not accepted. Check authorization consistently at every entry
point and resource access, including background/export/download paths. Scope queries to
the approved resource boundary, not a client-supplied tenant claim alone.

Build a matrix in the [review template](../templates/security-review.md): actor and
credential context, resource owner/tenant, operation, policy source, expected outcome,
observed outcome and evidence. Include horizontal and vertical privilege cases,
identifier substitution, membership revocation and bulk operations when relevant.
Do not assume an administrator may cross tenants; ask the policy owner when undefined.

Use synthetic identities/data to exercise enforcement and data leakage, not just status
codes. Record the reviewed revision and unresolved policy rows separately from confirmed
defects. Prefer centralized framework enforcement plus tests that cover alternate paths.

Source: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
Primary source inspected through its [official repository](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authorization_Cheat_Sheet.md).
