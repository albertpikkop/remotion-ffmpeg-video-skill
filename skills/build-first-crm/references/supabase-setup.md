# Supabase setup

Read this before any Supabase project, schema, Auth or key action. Supabase changes frequently.
Search the current Supabase documentation and read current connector descriptions before acting.
As of this skill's 3 September 2026 review, new tables may require explicit Data API exposure and
grants in addition to RLS.

Useful official topics:

- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Securing the Data API](https://supabase.com/docs/guides/api/securing-your-api)
- [Admin create user](https://supabase.com/docs/reference/javascript/auth-admin-createuser)
- [Password sign-in](https://supabase.com/docs/reference/javascript/auth-signinwithpassword)

## 1. Project gate

1. Check whether the student already has a suitable Supabase project.
2. If a new project is needed, list the student's organizations and ask which organization to use.
3. Fetch the current project cost for that exact organization.
4. Repeat the amount and recurrence in plain language and use the connector's cost-confirmation
   flow.
5. Ask before creating the project. Copy project and organization IDs exactly from tool results.
6. Wait for the project to become active before schema work.

Do not infer that a free plan means zero cost. Do not choose an organization for the student.

## 2. Refresh the current contract

Before writing SQL:

- fetch the Supabase changelog summary and scan relevant breaking changes;
- search current docs for RLS, Data API exposure, Auth user creation and publishable keys;
- inspect the live SQL tool descriptions and use the tool they currently require for DDL; and
- use a migration name in lowercase snake case when the connector requests one.

Do not paste a stale dashboard path or CLI command when the connected tool can perform the action.

## 3. Minimum schema

Adapt names only when the existing project already has a clear convention. Do not add tenant,
pipeline, automation or audit tables to this first loop.

```sql
create table if not exists public.crm_operators (
  user_id uuid primary key references auth.users(id) on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists public.enquiries (
  id uuid primary key default gen_random_uuid(),
  name text not null check (char_length(btrim(name)) between 2 and 80),
  mobile text not null check (char_length(btrim(mobile)) between 7 and 20),
  email text check (email is null or char_length(email) <= 254),
  message text check (message is null or char_length(message) <= 1000),
  consent_to_contact boolean not null check (consent_to_contact = true),
  source text not null default 'landing_page' check (source = 'landing_page'),
  created_at timestamptz not null default now()
);

alter table public.crm_operators enable row level security;
alter table public.enquiries enable row level security;

revoke all on table public.crm_operators from anon, authenticated;
revoke all on table public.enquiries from anon, authenticated;

grant select on table public.crm_operators to authenticated;
grant insert on table public.enquiries to anon, authenticated;
grant select on table public.enquiries to authenticated;

create policy "operator can read own membership"
on public.crm_operators
for select
to authenticated
using (user_id = (select auth.uid()));

create policy "visitor can submit valid enquiry"
on public.enquiries
for insert
to anon, authenticated
with check (
  char_length(btrim(name)) between 2 and 80
  and char_length(btrim(mobile)) between 7 and 20
  and (email is null or char_length(email) <= 254)
  and (message is null or char_length(message) <= 1000)
  and consent_to_contact = true
  and source = 'landing_page'
);

create policy "approved operator can read enquiries"
on public.enquiries
for select
to authenticated
using (
  exists (
    select 1
    from public.crm_operators
    where crm_operators.user_id = (select auth.uid())
  )
);
```

Before applying, inspect existing tables and policies. If these names already exist with different
meaning, stop and mark the collision `[PENDING]`. Do not drop or replace an existing table.

The schema deliberately creates no update or delete policy. The first dashboard is read-only.
There is deliberately no anonymous select policy.

## 4. Data API exposure

RLS controls rows after a table is reachable. Grants and the project's exposed-schema settings
control whether the Data API can reach it at all.

After the migration:

1. Confirm the intended schema is exposed to the Data API using the current project settings.
2. Confirm only the grants above are present for `anon` and `authenticated`.
3. Test an anonymous insert without requesting returned rows.
4. Test that an anonymous select is denied or returns no rows under RLS.

Never fix an access problem by disabling RLS or using a service-role key in the browser.

## 5. Operator account

Ask for the operator's real email. Generate a strong temporary password of at least 20 characters
using a cryptographically secure random source. Never put it in a file, terminal command, receipt,
URL, screenshot or repository.

Prefer a currently available Supabase admin API or connector that creates the user server-side. If
none exists, the Supabase dashboard is the last-resort setup path and requires the user's approval
before browser control. Create one email-and-password user and confirm the email through the
supported admin flow so the first login does not depend on SMTP.

The Supabase Admin create-user API is server-only. Never expose a secret or service-role key to the
Site to call it.

After Auth user creation, bind the returned user UUID to `public.crm_operators`. If the creation
path does not return the UUID, query `auth.users` by the exact normalized email using a safe SQL
literal, confirm exactly one match, then insert that UUID. Never grant access from user-editable
metadata.

Show the temporary password once only after the account and login are verified. Tell the student
to save it immediately in a password manager.

## 6. Browser configuration

Retrieve the project URL and one enabled modern publishable key. Use the legacy anon key only when
the current client or project requires compatibility. The project URL and publishable key may be
browser-visible. Secret keys and service-role keys may not.

Use clear environment names such as:

```text
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY
```

Keep local `.env` out of Git and provide placeholder names only in `.env.example`.

## 7. Database verification

- Run the connected security advisor after DDL and fix material findings.
- Run the performance advisor and record relevant findings without overbuilding.
- Confirm the operator row points to the created Auth user.
- Confirm anonymous insert succeeds for a valid record.
- Confirm anonymous select, update and delete do not expose or change records.
- Confirm the authenticated operator can select enquiries.
- Confirm another authenticated user without an operator row cannot select them if such a safe test
  account is available. Do not create extra live accounts only for this check without approval.
