# Authentication and sessions

Inspect the project's actual authentication method and threat model. Review recovery,
credential changes, sensitive actions, throttling and enumeration exposure. Prefer
maintained framework/provider controls and their version-matched guidance. Select MFA,
reauthentication and credential policy with the accountable owner rather than inventing
product requirements during implementation.

For sessions, inspect creation, renewal after privilege changes, expiry, logout/revocation
and storage/transport exposure. For browser cookies, assess Secure, HttpOnly and SameSite
against the actual navigation/authentication flow; there is no universal Strict setting
or token lifetime for every app. A JWT does not remove the need for issuer/audience,
signature, expiration and lifecycle checks appropriate to its use.

Test applicable invalid/expired/revoked credentials and recovery paths with synthetic
accounts. Record the configured policy and actual outcomes. Avoid copying arbitrary
algorithm or password-work-factor numbers from a generic skill into production.

Sources: [OWASP Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
and [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
Primary texts inspected in the official OWASP CheatSheetSeries repository; consult
current provider/framework documentation for implementation-specific configuration.
