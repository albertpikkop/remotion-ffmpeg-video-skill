# FFmpeg transforms and verification

Use this reference when inspecting, normalizing, editing, mastering, or validating media. Commands
are patterns: preserve the user's chosen output and derive parameters from the delivery contract.

## Inspect before changing

Generate machine-readable facts:

Commands are written on one line with double quotes so they paste into PowerShell, cmd and a
Mac terminal. `SKILL_DIR` means this skill's own folder (the script sits next to SKILL.md); on
Windows replace `python3` with `py -3`.

```bash
ffprobe -v error -show_format -show_streams -show_chapters -of json "/absolute/path/input.mov"
```

```bash
python3 "SKILL_DIR/scripts/media_audit.py" "/absolute/path/input.mov" --output "/absolute/path/input.audit.json"
```

Check stream order, start times, duration, average and real frame rates, time base, sample/display
aspect ratio, pixel format, colour range/space/transfer/primaries, rotation side data, audio sample
rate, channels, and layout. Treat missing colour metadata as unknown, not Rec.709 by default.

Run a full decode when corruption or final readiness matters:

```bash
python3 "SKILL_DIR/scripts/media_audit.py" "/absolute/path/candidate.mp4" --decode --sha256 --output "/absolute/path/candidate.audit.json"
```

`PASS` means the whole file decoded with zero errors. `PROBED` means no decode was run and
proves nothing about playback. `FAIL` lists the decode errors.

## Safe transform choices

- **Trim and re-encode:** use an accurate decoded trim when exact frames matter. Apply the same
  interval to all intended streams and inspect the new start/duration.
- **Stream copy:** use only when keyframe-level accuracy is acceptable and the source codecs,
  timestamps, and target container are compatible.
- **Concatenate:** use the concat demuxer for matching streams and the concat filter when sources
  need normalization or re-encoding.
- **Frame-rate normalization:** explicitly choose CFR only when the destination needs it. Record
  the chosen fps and verify motion and audio sync after conversion.
- **Orientation:** inspect rotation metadata and decoded display orientation. Decide whether to
  preserve metadata or bake rotation into pixels; do not accidentally do both.
- **Colour:** preserve a known colour pipeline, or perform an explicit transfer/primaries/matrix
  transform. Merely writing `-color_primaries`, `-color_trc`, or `-colorspace` changes signalling,
  not pixels. Review representative skin, highlight, shadow, and saturated-colour frames.
- **Audio:** choose targets from the delivery contract. For files, prefer a measured two-pass
  `loudnorm` workflow over an unmeasured one-pass change, then verify integrated loudness and true
  peak on the output.

For a conventional web/social H.264 delivery after colour is already correct, a starting shape is:

```bash
ffmpeg -n -i "/absolute/path/master.mov" -map "0:v:0" -map "0:a:0?" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "/absolute/path/delivery-v1.mp4"
```

Do not add Rec.709 tags to that command unless the signal was inspected and, when necessary,
actually converted. Use hardware encoding when turnaround requires it, but treat it as a distinct
delivery path and verify its output; hardware and software encoders are not byte-equivalent.

## Diagnose with focused evidence

Prefer short, attributable checks over speculative filter chains:

- extract stills at exact timestamps and around reported transitions;
- use `showinfo` or frame metadata when timestamp behavior is unclear;
- use `ebur128`/`loudnorm` measurement for audio levels;
- use `silencedetect`, `blackdetect`, or `freezedetect` only as candidate finders, then inspect the
  flagged moments;
- compare stream start times and durations before adding offsets or padding.

When a filter graph becomes complex, write it to a versioned filter script and keep the invocation
small. Name intermediate pads by their semantic role. Never interpolate untrusted text or paths
into a shell command; pass arguments as an array from scripts.

## Final receipt

Verify at least:

```bash
ffmpeg -v error -i "/absolute/path/candidate.mp4" -map "0:v:0?" -map "0:a:0?" -f null -
```

```bash
ffprobe -v error -show_format -show_streams -of json "/absolute/path/candidate.mp4"
```

A clean decode prints nothing. Any printed line is an error even when the exit code is 0.

Also inspect first, middle, transition, factual-card, and final frames. Record the exact command,
tool version, output SHA-256, decode result, video/audio starts and duration delta, resolution, fps,
codec/profile, pixel format, colour fields, audio format, and any accepted warning.
