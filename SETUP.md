# Setup for this skill

Everything for all three skills, per machine, is in the shared
[SETUP.md in noguess](https://github.com/albertpikkop/noguess/blob/main/SETUP.md). This skill
needs, from that list:

1. Node.js, the LTS installer from nodejs.org. Check: `node -v`.
2. FFmpeg. Mac: `brew install ffmpeg`. Windows: `winget install Gyan.FFmpeg`, then close and
   reopen the terminal. Check: `ffmpeg -version`.
3. Python 3. Mac has it (`python3 --version`). Windows: `winget install Python.Python.3.12`,
   check `py -3 --version`.

The skill scaffolds the Remotion project itself (`npx create-video@latest <folder> --blank`),
installs its packages and the render browser, and asks before each install. The first render
browser download is a few hundred megabytes and looks stuck for a minute; that is normal.
