# GrowTricity Student Skills

Beginner-friendly agent skills for building real projects with Codex.

This repository currently contains one standalone skill: `remotion-ffmpeg-video`.

The First CRM skill lives separately at
[albertpikkop/first-crm-skill](https://github.com/albertpikkop/first-crm-skill).

## Remotion + FFmpeg Video

Build, edit, render and verify reproducible programmatic videos. The skill helps choose between
Remotion, FFmpeg or a hybrid workflow and includes a deterministic media-audit script for
inspecting and validating files.

## Install

```bash
npx skills add albertpikkop/growtricity-student-skills -g
```

Remove `-g` if you want the skill only in the current project.

## Use

```text
Use $remotion-ffmpeg-video to build and verify this video: [describe the video and provide its files].
```

## Beginner exercise

Follow [EXERCISE.md](EXERCISE.md) to create and verify a six-second vertical video without
publishing it.

## Requirements

- An agent that supports `SKILL.md`, such as Codex.
- FFmpeg for media inspection and rendering.
- Node.js and Remotion when the project uses Remotion.

Rendering a video does not authorize upload, publication, scheduling or spend.

## Licence

MIT. See [LICENSE](LICENSE).
