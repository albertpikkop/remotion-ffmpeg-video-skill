# Verification and handoff

Read this before calling a CRM ready. Verify the produced system, not only source code or command
exit codes.

## Test record

Use one clearly fake record such as:

```text
Name: CRM Test Enquiry
Mobile: 9999999999
Email: crm-test@example.com
Message: End-to-end classroom verification. Safe to delete.
Consent: checked
```

Do not use a real customer's contact information for testing. If the business may already contain
a row with that label, add a visible date and time to make the test unique.

## Public journey

- Open the deployed landing page at a phone-sized viewport.
- Confirm the first screen names the correct business, offer and primary action.
- Confirm no `[PENDING]`, starter copy, invented claim or private operator link is visible.
- Trigger one validation error and confirm entered values remain.
- Fill the honeypot and confirm no record is created.
- Submit the valid labelled test enquiry once.
- Confirm one success message and exactly one matching database row.
- Confirm refreshing or double-clicking did not create a duplicate from the same action.

## Database and access

- Confirm RLS is enabled on `crm_operators` and `enquiries`.
- Confirm no anonymous select, update or delete policy exists for enquiries.
- Confirm the browser bundle and deployed source contain no secret or service-role key.
- Confirm the project uses an enabled publishable key.
- Confirm current Data API exposure and grants permit the intended insert and operator select only.
- Run Supabase security advisors and resolve material findings.
- Record performance-advisor findings that apply, without adding speculative optimization.

## Operator journey

- Open `/operator` while signed out and confirm it returns to login without showing enquiries.
- Sign in with the operator email and temporary password.
- Confirm the labelled test enquiry appears with the same name, contact details, message and time.
- Confirm empty optional fields render cleanly on another temporary local fixture if needed. Do not
  create another live row only for visual polish.
- Sign out and confirm the protected page no longer shows enquiry data.
- Confirm a failed login does not reveal whether the email exists.

## Usability and accessibility

- Test keyboard navigation and visible focus.
- Check labels, status announcements and error associations.
- Check narrow phone and normal desktop layouts for clipping, overlap and unreadable text.
- Confirm loading, empty, error, success and expired-session states exist and are understandable.

## Spec-only check

Before fixes, report:

```text
Invented: [anything not supported by BUSINESS-TRUTH.md]
Checks: [each check above marked met, not met or PENDING]
Assumed: [anything decided without approval]
Security: [advisor and manual access results]
Remaining risk: [especially public-form spam limits]
```

Fix only what the check surfaces, then rerun the affected journey.

## Handoff

Use one status: `ready`, `not ready`, or `blocked`.

For `ready`, give the non-technical student:

- the landing-page link;
- the operator-login link;
- the operator email;
- the temporary password once, with "Save this now";
- where new enquiries appear;
- which checks passed; and
- one honest sentence that basic form protection is not enough for high-volume public traffic.

Never include database IDs, keys, tokens, source credentials or raw tool output in the handoff.
