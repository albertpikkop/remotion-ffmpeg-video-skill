# First CRM product contract

Read this before choosing the data model, routes, form fields or dashboard layout.

## Users and jobs

### Visitor

The visitor needs to understand the business, decide whether it is relevant, and send one enquiry
from a phone without creating an account.

### Operator

The operator needs to sign in and answer one question: "Who enquired, what did they ask, and when?"

## Minimum routes

- `/`: business landing page and enquiry form.
- `/operator/login`: email and password sign-in.
- `/operator`: protected, read-only enquiry list and detail view.

Use different paths only when the generated Sites starter has a strong existing convention. Do not
add navigation to the private operator route from the public marketing header.

## Public landing page

Derive copy and visual direction from the approved `BUSINESS-TRUTH.md`.

The first screen must identify:

- the business;
- what it helps the customer do;
- who or where it serves; and
- one clear action that moves to the enquiry form.

Include only sections supported by real business facts. A small page usually needs the first-screen
promise, the offer or services, supplied proof if any, practical contact details, and the enquiry
form. Omit empty testimonial, statistics, team, pricing or FAQ sections instead of inventing them.

Use a coherent theme derived from the business. Do not leave starter styling or generic AI gradient
design as the final appearance. Keep controls readable, touch targets comfortable and the form
usable on a narrow phone.

## Enquiry form

Default fields:

- Name, required, 2 to 80 characters.
- Mobile number, required, normalized and 7 to 20 characters after allowed punctuation.
- Email, optional, maximum 254 characters and validated when supplied.
- Enquiry message, optional, maximum 1,000 characters.
- Contact consent, required: "[Business] may contact me about this enquiry."
- Company website, hidden honeypot, must remain empty.

Do not describe enquiry consent as marketing consent. Do not add a newsletter checkbox. Do not ask
for sensitive identity, financial or health information in the first CRM.

States:

- Ready: form can be completed.
- Sending: submit is disabled and status is announced.
- Success: confirms receipt without promising a response time the business did not supply.
- Validation error: identifies the field and preserves the entered values.
- Service error: apologizes plainly and offers the verified public phone or email when available.
- Duplicate click: one client request is sent and the button remains disabled until it resolves.

## Operator experience

Login asks only for operator email and password. Use a visible show-password control, a clear error
that does not reveal whether an account exists, and an accessible loading state.

The protected screen starts with the work, not a marketing hero. Show:

- business name;
- sign-out control;
- enquiry count for the loaded result;
- newest enquiries first;
- name, mobile, optional email, message and submitted time; and
- clear loading, empty, error and signed-out states.

Escape all enquiry text. Phone and email actions may use `tel:` and `mailto:` after validation.
Do not add status editing, assignment, exporting, deletion or messaging in version one.

## Data contract

The public client inserts these fields into `public.enquiries`:

```text
id                 generated UUID
name               required text
mobile             required text
email              optional text
message            optional text
consent_to_contact required true
source             landing_page
created_at         generated timestamp
```

`public.crm_operators` contains only the authenticated operator user IDs allowed to read enquiries.
The public form does not supply an owner ID, role or authorization flag. This is one Supabase
project for one student's business, so there is no browser-selected tenant.

## Honest security boundary

RLS and validation prevent public reads and malformed inserts. A honeypot and client cooldown stop
accidental repeats and basic bots. They do not provide strong high-volume rate limiting. Before a
real paid campaign or meaningful traffic, add a server-side per-IP limit or managed challenge
through the hosting environment and re-run verification.
