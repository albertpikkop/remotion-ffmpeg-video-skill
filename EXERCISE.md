# Exercise 2: Make and verify a programmatic video

## What you will prove

You can build a short Remotion composition, render it, watch it, and verify the produced MP4
with FFmpeg instead of trusting the render command.

## Before you start

The three tools in [SETUP.md](SETUP.md). The skill checks them and tells you the one command to
run if one is missing.

## Copy this into your agent

Codex: start with `Use $remotion-ffmpeg-video to ...`. Claude Code and others: just paste it.

```text
Create a six-second vertical video for local review only.
Canvas: 1080 by 1920. Frame rate: 30 fps. Background: deep navy, #0B1F3A.
Font: Inter, loaded through Remotion's Google Fonts package.
Opening text: My first programmatic video
Closing text: Built with frames, not guesses
Only text and simple geometric shapes. No stock media, logo, music or voice.
Keep the source editable in Remotion.
Render a new MP4, show me the first and last frame, run a full decode, make a SHA-256 receipt,
and do not upload or publish it.
```

## What should happen

1. The agent checks FFmpeg, Node and Python, and scaffolds the Remotion project, asking before
   each install.
2. It records the contract: six seconds, 1080 by 1920, 30 fps, H.264, navy #0B1F3A, Inter.
3. It renders two still frames, gives you their paths, and asks you to look.
4. It renders once, straight to H.264, then verifies the file with `media_audit.py --decode`.
5. It asks you to play the file start to end.
6. It hands off: output path, receipt, `ready`, no upload happened, then the check.

## Pass check

- You opened the MP4 and watched all six seconds.
- The two lines of text are readable in the two frames.
- Duration between 5.9 and 6.1 seconds; resolution 1080 by 1920; 30 fps.
- The audit says `PASS` (a full decode with zero errors), not `PROBED`.
- The receipt contains the output SHA-256.
- No upload, publish or spend happened.
