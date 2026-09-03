# GrowTricity Student Skills

Beginner-friendly agent skills for building real projects with Codex.

This repository contains two independent skills. Install only the one you need.

## Skills

### Build My First CRM

Turn an approved business plan into a small working CRM:

```text
Landing page -> enquiry form -> Supabase -> operator login -> enquiry list
```

The skill is designed for non-technical students. It checks what is installed, explains missing
connections in plain language, verifies Supabase cost before creating a project, and asks before
external account changes or deployment.

### Remotion + FFmpeg Video

Build, edit, render and verify reproducible programmatic videos. It helps choose between Remotion,
FFmpeg or a hybrid workflow and includes a media-audit script for inspecting and validating files.

## See what is available

```bash
npx skills add albertpikkop/growtricity-student-skills --list
```

## Install one skill

Install the CRM skill:

```bash
npx skills add albertpikkop/growtricity-student-skills --skill build-first-crm -g
```

Install the video skill:

```bash
npx skills add albertpikkop/growtricity-student-skills --skill remotion-ffmpeg-video -g
```

Remove `-g` if you want the skill only in the current project.

## Try it

For the CRM:

```text
Use $build-first-crm to build my first CRM from this business plan: [paste or attach the plan].
```

For video:

```text
Use $remotion-ffmpeg-video to build and verify this video: [describe the video and provide its files].
```

The skill will ask for confirmation before consequential external changes. Installing a skill does
not authorize it to create a paid project, connect an account, publish a site, upload a video or
spend money.

## Beginner exercises

- [Exercise 1: Build a first CRM](exercises/01-build-first-crm.md)
- [Exercise 2: Make and verify a programmatic video](exercises/02-remotion-ffmpeg-video.md)

## Requirements

- An agent that supports `SKILL.md`, such as Codex.
- The CRM workflow needs the Supabase and Sites capabilities connected in the student's agent.
  If either is unavailable, the skill stops and asks before using a supported installation or
  connection flow.
- The video workflow needs FFmpeg for media inspection and rendering, and Node.js plus Remotion for
  Remotion projects.

Each student should use their own Supabase project. Do not put different students' customer data in
one shared classroom database.

## Licence

MIT. See [LICENSE](LICENSE).
