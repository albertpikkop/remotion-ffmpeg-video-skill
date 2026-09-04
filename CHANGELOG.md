# Changelog

## v0.2.0, 4 September 2026

Rewritten after a cold review of the skill and a second cold review of the three-skill journey.

- Plugin layout, so one marketplace (`ashishpunj`) installs all three skills on Claude Code.
- Stage 0, the machine first: FFmpeg, Node, Python checks with the install command per system,
  a non-interactive scaffold, the render browser fetched once, the audit script by absolute
  path, every command Windows-safe. Asks before installing anything.
- A beginner front door: reads `BUSINESS-TRUTH.md`, a default contract (1080 by 1920, 30 fps,
  H.264, local review) as labelled assumptions, at most three questions, stand-down for small
  edits, tell-before-change for existing projects.
- `media_audit.py`: a decode with errors is `FAIL`; a probe alone is `PROBED`, never `PASS`;
  the receipt no longer swallows the output on a rerun.
- Checks the student does: play the file, open two frames, carried as [PENDING] until answered.
- One direct H.264 render for graphics-only work; lower concurrency when unstable.
- The check in the noguess shape with an inline fallback; Next time into the truth file.
- Exercise: a named font, a hex colour, a duration window, and "you watched it".

## v0.1.0, 3 September 2026

First public version.
