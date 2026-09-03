# Remotion authoring and rendering

Use this reference for Remotion composition work. Keep creative approval and platform actions in
their owning workflows.

## Preflight

Inspect `package.json`, the lockfile, the Remotion entry point, registered compositions, render
scripts, public assets, fonts, and any props schema. Run the package manager's dependency listing
before changing versions. Keep `remotion`, `@remotion/cli`, `@remotion/renderer`, and any other
Remotion packages on one compatible, pinned version already used by the project.

Use the current project's media component and API surface. In a new or deliberately upgraded
current-v4 project, `<Video>` from `@remotion/media` is the preferred embedded-video component. Do
not introduce it into an older locked project without checking that its installed version and
render path support it.

## Composition contract

- Give each composition a stable ID and explicit `width`, `height`, `fps`, and
  `durationInFrames`.
- Put changing content in typed, serializable input props rather than forking components.
- Use `calculateMetadata()` when props determine dimensions, fps, duration, or normalized props.
- Pass the same input props when selecting and rendering a composition programmatically.
- Centralize the seconds-to-frames rule. Round once and make adjacent ranges contiguous; do not
  independently round every boundary and accumulate gaps.
- Keep timeline data separate from presentation components when the edit has multiple beats.
  Give each beat a stable ID, start frame, duration, visual job, audio source, and source range.

Use `<Sequence>`, `useCurrentFrame()`, and `useVideoConfig()` for timeline-relative work. Use
`staticFile()` for files in the public directory. Remote assets must be versioned or cached before
a final render; a changing URL makes the render non-reproducible.

## Determinism

Every frame must be a pure consequence of frame number, props, and locked assets. Avoid
`Date.now()`, unseeded randomness, live API calls, machine-local font substitution, mutable remote
URLs, and layout that depends on asynchronous data arriving unpredictably. Materialize external
data before rendering. Load fonts and assets deterministically and fail the render if a required
asset is missing.

Use `interpolate()` with explicit extrapolation and `spring()` with the composition fps. Motion
must finish inside the intended beat; a spring that happens to settle later is not a timing plan.
Test animation boundaries at the frame before, the boundary frame, and the frame after.

## Render loop

Use the repository's local CLI and lockfile, for example:

```bash
npx remotion compositions src/index.tsx
npx remotion still src/index.tsx CompositionId /absolute/path/frame.png --frame=0 --props=/absolute/path/props.json
npx remotion render src/index.tsx CompositionId /absolute/path/candidate.mp4 --props=/absolute/path/props.json
```

For a programmatic renderer, bundle the entry point, call `selectComposition()` with the input
props, then pass the resulting composition and the same props to `renderMedia()`. Use an explicit
output path and set overwrite behavior deliberately. Prefer supported renderer options over
`ffmpegOverride`; the latter depends on Remotion's internal FFmpeg command and can break across
patch releases.

Start with representative stills or a short frame range. A complete review set normally includes:

- first visible frame and first 500 ms;
- each layout and typography family;
- frames immediately around every sequence boundary;
- entry, hold, and exit of overlays and captions;
- each factual or numerical card; and
- the last spoken line and final frame.

Inspect those images, then render the candidate. Increase concurrency only after measuring host
memory and stability. Faster rendering is not useful if media decoding or browser memory becomes
nondeterministic.

## Hybrid boundary with FFmpeg

Normalize difficult camera sources before Remotion when browser decoding, variable frame rate,
rotation, HDR, unusual audio, or huge source files make frames unreliable. Keep a manifest that
maps every normalized proxy to its original and transform command.

Let Remotion own composition and graphic timing. Let the final FFmpeg stage own the declared
delivery encode, container flags, loudness pass, and machine-verifiable media receipt. Do not use a
post-render FFmpeg filter to move or repaint graphics that should remain editable in React.
