---
name: build-first-crm
description: >-
  Build a non-technical user's first working CRM from a business plan using Sites for the landing
  page and operator dashboard and Supabase for enquiry storage and email-password login. Use when
  someone says "build me my first CRM", wants a simple business enquiry system, or needs the full
  landing-page-to-lead-list loop. Do not use for an existing complex CRM, messaging automation,
  billing, analytics, or enterprise architecture.
---

# Build My First CRM

## Outcome

Turn an approved business plan into one small working loop:

```text
Visitor opens landing page
Visitor sends enquiry
Supabase stores enquiry
Operator signs in
Operator sees the same enquiry
```

The student and operator may be using these tools for the first time. Speak in plain language,
make one recommendation at each decision, and keep technical detail behind the work unless the
person must act on it.

## Fixed first-version boundary

Build only:

- one responsive business landing page;
- one enquiry form;
- one student-owned Supabase project;
- one operator email-and-password login;
- one protected, read-only enquiry dashboard; and
- one verified test enquiry through the real form.

Do not add a pipeline, automated messages, billing, analytics, multiple staff roles, file uploads,
customer login, or multi-tenant SaaS architecture. Do not put different students' customer data in
one classroom Supabase project.

## Know the current stage

The person never repeats a stage. Read the conversation and any generated `BUSINESS-TRUTH.md`:

1. **No approved business truth:** run the intake and stop for confirmation.
2. **Truth approved, capabilities unknown:** check the live skill and tool registry.
3. **Capabilities ready, external actions not approved:** show the exact action and any cost, then
   wait.
4. **Build approved:** create the database and operator access, then build the Site.
5. **Build present:** run the real loop checks before calling it ready.

## Stage 1: approve the business truth

Read [references/business-intake.md](references/business-intake.md) when the user first supplies a
business plan, notes, document, or raw description.

Create `BUSINESS-TRUTH.md` from [assets/BUSINESS-TRUTH-TEMPLATE.md](assets/BUSINESS-TRUTH-TEMPLATE.md)
only after reviewing the source. Separate facts, assumptions and missing information. Ask no more
than three easy questions whose answers change the landing page or enquiry flow. Do not invent a
business name, offer, price, address, phone number, proof, logo, colour, legal claim or testimonial.

Show the short truth back to the user and ask, "Is this correct?" Do not initialize a Site, create
a Supabase project or install a capability before they approve it.

## Stage 2: check capabilities

Inspect the current registry instead of relying on remembered availability:

- Supabase needs connected tools for projects, costs, SQL, keys and advisors.
- Sites needs the installed `sites-building` and `sites-hosting` skills and its connector tools.

If either capability is missing, say which one is missing and why it is needed. Use the environment's
supported plugin suggestion or connection flow only after the user agrees. Never install a plugin
through an unreviewed shell command. If no supported installation path is available, stop with
`[PENDING: connect or install Supabase/Sites]` and give one plain next step.

Installing this skill is not permission to create projects, accept costs, deploy publicly or change
an account.

## Stage 3: show the preflight and get approval

Before external writes, show one short summary:

```text
Business: [approved name]
Will create: [Supabase project, database tables, operator account, Site]
Will publish: [private/public and why]
Cost: [verified amount and recurrence, or no added cost]
Operator login: [email; password will be generated and shown once]
Still missing: [PENDING items, or none]
```

For a new Supabase project, always identify the student's organization, fetch the current project
cost for that organization, repeat the amount and recurrence, and use the connector's cost
confirmation flow. Ask before creating the project. If the user already has a suitable project,
offer to reuse it and do not create another one automatically.

Ask immediately before any public or shared Site deployment using the access wording required by
the installed Sites hosting skill. A private owner-only deployment follows the current Sites rules.

## Stage 4: build the loop

Read these references only when their part begins:

- [references/crm-contract.md](references/crm-contract.md) before schema or interface work.
- [references/supabase-setup.md](references/supabase-setup.md) before any Supabase write.
- [references/sites-build.md](references/sites-build.md) before initializing or editing the Site.

Follow current Supabase documentation and current connector descriptions. They change over time.
Follow the installed Sites skills rather than copying old setup, packaging or deployment commands.

Keep the build order:

1. Create or select the approved Supabase project.
2. Create the schema and row-level security.
3. Create the operator Auth user and bind that user's ID to the operator table.
4. Retrieve only the project URL and an enabled publishable key for browser use.
5. Build the landing page, form, login and dashboard through Sites.
6. Configure runtime values through Sites. Keep local `.env` and `.env.example` aligned.
7. Validate locally, then deploy only through the current Sites hosting workflow.

Generate a strong temporary operator password with a cryptographically secure random source. Do
not save it in source, environment examples, receipts, screenshots, shell history or GitHub. Show
it once in the private handoff and tell the user to save it in a password manager. Use the operator
email as the login identifier. Do not invent a separate username system.

## Security and privacy contract

- Treat every public form value and browser-visible ID as attacker-controlled.
- Enable RLS on every exposed table before inserting real customer data.
- Anonymous visitors may insert a valid enquiry but may never select, update or delete enquiries.
- An authenticated account may read enquiries only when its user ID exists in the CRM operator
  table. `TO authenticated` without an ownership check is not authorization.
- Use explicit Data API grants when the project requires them. Grants and RLS are separate gates.
- Use only an enabled Supabase publishable key in browser code. Never use a secret or service-role
  key in the Site, repository, logs or chat output.
- Validate and length-limit every field. Escape rendered enquiry text. Include a honeypot and a
  short client submission cooldown, but describe these honestly as basic classroom protection,
  not high-volume bot defence.
- Collect only information needed to answer the enquiry. Do not combine enquiry consent with
  marketing consent.
- Do not expose raw errors, internal paths or stack traces to visitors.

## Stage 5: prove it

Read [references/verification.md](references/verification.md). Do not declare success from a build
command or API receipt alone. Use one clearly labelled test enquiry and prove the full external
loop. Run Supabase security and performance advisors after schema work and resolve material
security findings before handoff.

Final status must be one of `ready`, `not ready`, or `blocked`. A ready handoff tells the student:

- the landing-page URL;
- the operator login URL and email;
- the temporary password once, with a save-now instruction;
- what the form collects;
- where enquiries appear;
- the result of every visible check; and
- the remaining classroom-MVP risk, especially public-form spam limits.

Never claim a Site is public, a project exists, a form stored data, or an operator can log in
without a current receipt or direct verification.
