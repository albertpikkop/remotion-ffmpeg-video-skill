# Sites build

Read this after Supabase is ready and before initializing or editing the Site.

## Use the live Sites workflow

Load the installed `sites-building` skill completely, including the environment reference it
requires for setup and preview. This CRM uses external data and authentication, so follow its
capability path. After validation, load `sites-hosting` and follow its current publication and
access-control rules.

Do not copy hosting commands from this reference. Sites owns project initialization, source
credentials, packaging, saved versions, deployment and access. Never call site creation twice for
the same `.openai/hosting.json`.

## Product shape

Build three routes:

- `/`, business landing page and enquiry form;
- `/operator/login`, operator sign-in; and
- `/operator`, protected enquiry dashboard.

Use the generated project's existing package manager and lockfile. Pin any added Supabase client
package version. Keep the framework and Cloudflare-compatible output selected by Sites.

## Environment values

The browser may receive only:

- the Supabase project URL; and
- an enabled Supabase publishable key.

Configure hosted values through Sites. Keep `.env` and `.env.example` names aligned, but commit
only placeholders in `.env.example`. Search the full deployable source for secret-key formats and
service-role references before publishing.

## Landing page

- Use only facts from `BUSINESS-TRUTH.md`.
- Put the business, customer promise and primary enquiry action in the first viewport.
- Infer one coherent visual direction from the real business or supplied brand.
- Do not leave starter copy, starter theme values or generic dashboard styling.
- Use supplied images first. Follow the installed Sites imagery rules when no suitable image is
  supplied.
- Keep the public contact method visible near the form when one was approved.
- Do not link the private operator route from the public navigation.

## Form implementation

- Use proper labels, input modes and autocomplete values.
- Normalize and validate fields before sending.
- Keep a hidden honeypot outside keyboard navigation and reject the submission when it is filled.
- Disable duplicate submission while a request is pending and add a short client cooldown.
- Insert without chaining `.select()`, because anonymous visitors have no read permission.
- Send only the approved fields. Never send role, operator ID or an authorization flag from the
  browser.
- Announce loading, validation, success and service-error states accessibly.
- Escape any user-controlled text that later appears in the dashboard.

## Authentication and route protection

Use the current Supabase password sign-in API. Show one generic failure message for invalid login.
Do not reveal whether an email exists.

Protect `/operator` using the strongest route-level session check supported by the generated Sites
stack. Redirect signed-out visitors to `/operator/login`. Treat frontend hiding as usability, not
authorization. Supabase RLS remains the data boundary even if someone loads the route directly.

Provide sign out. Do not provide public signup, password reset or staff invitations in version one.

## Dashboard

Show the work immediately:

- business name and sign out;
- newest enquiries first;
- name, mobile, optional email, enquiry message and submitted time;
- tap-friendly phone and email actions after validation; and
- visible loading, empty, error and expired-session states.

Do not add charts, vanity metrics, side navigation, role controls or empty dashboard cards.

## Preview and deployment

Follow the installed Sites first-meaningful-preview rule. The preview must already show the real
business direction and primary enquiry action, not a starter skeleton.

Because the form changes data, apply the current Sites WebMCP guidance after the first meaningful
preview if the installed skill requires it.

Build successfully before hosting. A public or shared deployment needs the exact user approval
required by the current hosting skill. A deployed URL is production. Do not call the site ready
until the full form-to-dashboard verification passes against that exact deployment.
