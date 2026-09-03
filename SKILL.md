---
name: remotion-ffmpeg-video
description: Build, edit, render, debug, and verify programmatic video workflows with Remotion and FFmpeg. Use when React-based compositions, template-driven motion graphics, automated video variants, media normalization, trimming, muxing, encoding, colour or audio handling, frame extraction, or render diagnostics are central; do not use for creative direction alone or for publishing.
---

# Remotion + FFmpeg Video

## Outcome

Produce a reproducible video build whose inputs, timeline, render settings, mastering command, and
verification can be inspected and rerun. Preserve source media and prior candidates. A render is a
local artifact, not permission to upload, publish, schedule, replace, or spend money.

## Choose the smallest suitable path

- **Remotion:** data-driven motion graphics, captions, reusable React/SVG scenes, repeatable visual
  systems, or many variants from one composition.
- **FFmpeg:** inspection, normalization, precise media transforms, trims, concatenation, audio
  processing, codec/container conversion, muxing, samples, and decode checks.
- **Hybrid:** normalize irregular source media with FFmpeg, compose with Remotion, then master and
  verify once with FFmpeg. This is the normal path when live footage and designed graphics meet.

Read [references/remotion.md](references/remotion.md) when authoring or rendering a Remotion
project. Read [references/ffmpeg.md](references/ffmpeg.md) when changing or validating media.

For story, shot design, or AI generation, use the relevant directing workflow before this skill.
For release-grade editorial acceptance, also run any applicable professional video-review skill on
the rendered candidate. Project-specific skills and the nearest `AGENTS.md` remain authoritative.

## Working contract

1. Read the nearest project instructions and inspect the existing package manager, lockfile,
   scripts, compositions, media conventions, and output folders before adding anything.
2. Inventory every input. Run `scripts/media_audit.py` on each source whose timing, orientation,
   colour, or audio matters. Treat rotation metadata and HDR/HLG/PQ tags as material facts.
3. Lock the delivery contract: canvas, aspect ratio, fps, duration, codec/container, audio target,
   colour space, alpha requirement, and review versus final purpose. Label assumptions when the
   request leaves a harmless choice open.
4. Use one master clock. Keep source decisions in seconds or timestamps, convert to integer frames
   once at the composition boundary, and apply the same trims and speed changes to picture and
   sound.
5. Preserve dependency and render reproducibility. Reuse the repository's package manager and
   pinned Remotion family version. Do not upgrade a mature project or install `latest` merely to
   complete an edit.
6. Prove representative frames before a costly full render: first frame, every layout family,
   timing boundaries, transitions, factual cards, and final frame. Inspect the actual images.
7. Avoid serial lossy encodes. Prefer one high-quality Remotion render or mezzanine followed by one
   delivery encode. Keep intermediates lossless or visually lossless when another encode follows.
8. Verify the produced file, not only the source code or exit code. Probe it, decode it end to end,
   compare A/V starts and durations, inspect frame samples, and confirm the declared delivery
   contract.

## Non-negotiable media rules

- Never guess fps, duration, orientation, stream order, channel layout, or colour characteristics.
  When a fact cannot be read from the file or the brief, write `[PENDING: what would settle it]`
  and stop; a receipt with a visible gap beats a render built on a guess.
- Assigning Rec.709 tags does not convert HDR/HLG/PQ pixels to Rec.709. Perform and verify a real
  transform when the delivery contract requires one.
- Do not let independent video and audio padding conceal a sync error. Repair the shared timeline.
- Use the concat demuxer only for stream-compatible files; use the concat filter and re-encode when
  inputs differ. Never concatenate arbitrary media with shell byte concatenation.
- Default to a new versioned output. Use overwrite only for explicitly disposable generated files.
- Do not declare a visual pass from one convenient frame. Inspect entry, hold, and exit states.

## Handoff

Return the source inventory, composition ID and props or FFmpeg command, output path, relevant
version/lock information, SHA-256 for an immutable candidate, probe/decode receipt, sampled-frame
paths, repaired defects, and one of `ready`, `not ready`, or `blocked`. State explicitly whether any
platform action occurred. Then run the check from the `noguess` skill (students say "TCE this"; `/tce` is its alias) on the candidate against the
delivery contract: invented, each check met or not met or [PENDING], assumed without being told,
why, the fix, and the one line to add to the next brief.
