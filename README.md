# remotion-ffmpeg-video

An agent skill for building, rendering and verifying programmatic video with Remotion and FFmpeg.
This repository installs that one skill. It was first published as `growtricity-student-skills`;
that name still redirects here.

**Level, plainly:** the rules inside are professional-grade (colour tags, frame timing, lossless
intermediates, verified renders). You do not need to know those words; the agent does. What you
need is the exercise below, which asks for a six-second video and checks the result the way a
professional would.

The First CRM skill lives separately at
[albertpikkop/first-crm-skill](https://github.com/albertpikkop/first-crm-skill).

## Remotion + FFmpeg Video

Build, edit, render and verify reproducible programmatic videos. The skill helps choose between
Remotion, FFmpeg or a hybrid workflow and includes a deterministic media-audit script for
inspecting and validating files.

## Install

```bash
npx skills add albertpikkop/remotion-ffmpeg-video-skill -g
```

Remove `-g` if you want the skill only in the current project.

## Use

```text
Use $remotion-ffmpeg-video to build and verify this video: [describe the video and provide its files].
```

## The method underneath

The skill follows the TCE + NHA loop ([albertpikkop/tce-skill](https://github.com/albertpikkop/tce-skill)):
it locks a delivery contract before rendering, marks any media fact it cannot read as [PENDING]
instead of guessing, and ends with a check of the produced file against that contract. Install
`tce` first and both skills share one loop:

```bash
npx skills add albertpikkop/tce-skill
```

The same `npx skills add` commands work for Claude Code, Codex and Cursor.

## Beginner exercise

Follow [EXERCISE.md](EXERCISE.md) to create and verify a six-second vertical video without
publishing it.

## Requirements

- An agent that supports `SKILL.md`: Codex, Claude Code or Cursor.
- FFmpeg for media inspection and rendering.
- Node.js and Remotion when the project uses Remotion.

Rendering a video does not authorize upload, publication, scheduling or spend.

## Licence

MIT. See [LICENSE](LICENSE).
