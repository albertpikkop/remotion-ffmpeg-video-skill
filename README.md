# remotion-ffmpeg-video

A skill for making and verifying a first programmatic video with Remotion and FFmpeg, and for
checking the file rather than trusting the render command. Third of three skills that share
one method and one file: [noguess](https://github.com/albertpikkop/noguess-prompt-skill) (the TCE + NHA
loop) and [build-first-crm](https://github.com/albertpikkop/first-crm-skill). All three read
and write `BUSINESS-TRUTH.md`, so the business is explained once.

**Level, plainly:** the rules inside are professional-grade (colour tags, frame timing,
verified renders). You do not need to know those words; the agent does. What you need is the
exercise, which asks for a six-second video and checks the result the way a professional
would. For a beginner the skill uses a default contract (1080 by 1920, 30 fps, H.264, local
review only) and asks at most three questions.

## Before you start

Day-one setup for all three skills is in the shared
[SETUP.md](https://github.com/albertpikkop/noguess-prompt-skill/blob/main/SETUP.md). This repo's own
[SETUP.md](SETUP.md) lists what this skill needs: Node.js, FFmpeg, Python 3. The skill checks
them first and prints the one install command for your system if one is missing, and it
scaffolds the Remotion project itself, asking before every install.

## Install

**Claude Code** (one marketplace for the three skills):

```bash
claude plugin marketplace add albertpikkop/noguess-prompt-skill
```

```bash
claude plugin install remotion-ffmpeg-video@ashishpunj
```

**Any agent, from GitHub:**

```bash
npx skills add albertpikkop/remotion-ffmpeg-video-skill
```

**Codex, by hand:** copy `skills/remotion-ffmpeg-video` into `~/.codex/skills/` on Mac or
`%USERPROFILE%\.codex\skills\` on Windows.

## Use

Say what you want in plain words: "make a 20 second video for my Diwali boxes". Codex users
can type `Use $remotion-ffmpeg-video to make ...`. The skill reads `BUSINESS-TRUTH.md` for the
facts, labels its assumptions, renders, verifies the file with a full decode, asks you to play
it, and ends with the noguess check.

## Beginner exercise

[EXERCISE.md](EXERCISE.md): a six-second vertical video, verified, never uploaded.

## What is in the skill

- `skills/remotion-ffmpeg-video/SKILL.md`: the stages. The machine first, the brief, the
  build, verify the file, the handoff and the check.
- `references/remotion.md` and `references/ffmpeg.md`: the composition rules and the media
  commands, written on one line with double quotes so they paste into Windows and Mac alike.
- `scripts/media_audit.py`: probes and decodes a file; `PASS` only after a clean full decode.
- `evals/`: the test asks and the checks used to grade it.

## Requirements and licence

Node.js, FFmpeg, Python 3, and an agent that reads `SKILL.md` (Codex, Claude Code, Cursor).
Remotion has its own licence: free for individuals and small teams, paid above that; check it
before company use. This skill is MIT (see [LICENSE](LICENSE)). Rendering a video does not
authorize upload, publication, scheduling or spend.
