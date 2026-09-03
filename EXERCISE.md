# Exercise 2: Make and verify a programmatic video

## What you will prove

You can build a short Remotion composition, render it locally, and verify the produced MP4 with
FFmpeg instead of trusting the render command alone.

## Copy this into Codex

```text
Use $remotion-ffmpeg-video to create a six-second vertical video for local review only.

Canvas: 1080 by 1920.
Frame rate: 30 fps.
Background: deep navy.
Opening text: My first programmatic video
Closing text: Built with frames, not guesses
Use only text and simple geometric accents. No stock media, logo, music or voice.
Keep the source editable in Remotion.
Render a new MP4, inspect representative frames, run a full decode, create a SHA-256 receipt and do
not upload or publish it.
```

## What should happen

1. Codex records the six-second, 1080 by 1920, 30 fps delivery contract.
2. It keeps the Remotion package family on one pinned version.
3. It inspects still frames before the complete render.
4. It verifies the actual MP4 with FFmpeg and `media_audit.py`.
5. It reports the composition, output, hash, media facts and sampled frames.
6. It states that no upload or publication occurred.

## Pass check

- Duration is six seconds within normal container tolerance.
- Resolution is 1080 by 1920 and frame rate is 30 fps.
- The full decode succeeds.
- The receipt contains the output SHA-256.
- The opening and closing text are readable in sampled frames.
- No platform action occurs.
