# Secrets and evidence

Inventory how scoped components receive secrets, which identities can read them, how
they rotate/revoke and how failure/recovery works. Use the project's approved secret
store or delivery mechanism; environment variables are not the only possible mechanism
and do not by themselves provide access control or rotation.

Inspect least-privilege access, lifecycle ownership, auditability and secret exposure in
source, generated artifacts, CI, logs and error output. Record identifiers/locations and
redacted reproduction, never the secret value. Synthetic credentials suffice for most
tests. If a real exposure is found, notify the authorized incident owner and follow the
approved revocation/remediation path; do not publish the credential in the finding.

Verify rotation/recovery claims only where the environment and authority allow actual
checks; otherwise report them as unverified with prerequisites. Separate application
behavior from platform guarantees you have not inspected.

Source: [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html),
inspected through the [official source](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Secrets_Management_Cheat_Sheet.md).
