# Scoped boundary review

Use this worksheet to choose review questions for the actual change. It is not a claim
of exhaustive security coverage or a substitute for version-specific implementation guidance.

| Changed boundary | Review question | Evidence to request |
|---|---|---|
| Input or shared schema | Where are shape, limits, coercion and business invariants enforced? | Accepted contract, invalid/boundary cases, server-side behavior |
| Output/export/log | Which fields and recipients are permitted, and how is content interpreted? | Data classification, policy, representative output and redacted logs |
| File/path/network target | Which destinations/resources can the caller influence? | Allowable boundary, validation and controlled negative cases |
| Dependency/configuration | What exact version/settings changed and which controls rely on them? | Lock/config diff, applicable advisories and relevant verification |
| External side effect | What protects authorization, retry/concurrency and abuse limits? | Approved semantics, isolated reproduction and recovery behavior |

Record expected behavior from project policy/contract. Missing evidence creates a gap
with an owner; infer a vulnerability only when code or reproduction supports it. Mark
findings with affected revision, impact, likelihood, assumptions and retest requirements.
Operational commands and real targets require appropriate task authority.
