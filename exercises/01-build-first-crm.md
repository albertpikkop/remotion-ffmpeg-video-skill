# Exercise 1: Build your first CRM

## What you will prove

A visitor can send an enquiry from a business landing page and the business operator can sign in
and see the same enquiry.

Use a fictional business for this classroom exercise. Do not enter a real customer's information.

## Copy this into Codex

Replace `[your email]` with an email address you control.

```text
Use $build-first-crm to build my first CRM.

Here is the business plan:
- Business name: Sunrise Yoga Studio. This is a fictional classroom business.
- Location: Mohali.
- Offer: beginner yoga classes in small groups.
- Main customer: adults who have never joined a yoga class.
- Main action: ask for a free introductory session.
- Hours: Monday to Saturday, 7 AM to 8 PM.
- Public phone number: not decided yet.
- Operator email: [your email].
- Brand direction: calm, warm and simple. Use cream, deep green and terracotta.
- No logo, prices, testimonials or certifications exist yet.
```

## What should happen

1. Codex restates the business facts and marks the missing phone number instead of inventing it.
2. You approve or correct the short business truth.
3. Codex checks whether Supabase and Sites are connected.
4. Before creating a Supabase project, Codex shows the current cost and asks for confirmation.
5. Before public or shared deployment, Codex asks for the required publication approval.
6. The final test uses a clearly fake enquiry.

## Pass check

- The page opens on a phone-sized screen.
- The form creates exactly one test enquiry.
- A signed-out visitor cannot read enquiries.
- The operator can sign in and see the same test enquiry.
- No password or secret key appears in the repository or browser source.

Stop the exercise if Codex invents the missing phone number, skips the cost confirmation, shares a
secret key, or calls the CRM ready without testing the form-to-dashboard loop.
