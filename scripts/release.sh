#!/usr/bin/env bash
# Release a new version of the remotion-ffmpeg-video skill.
#   scripts/release.sh 0.3.0 "one line on what changed"
# Checks the changelog has the section and no banned dashes, bumps plugin.json, packages
# dist/remotion-ffmpeg-video.skill (the skill folder without evals), commits, tags, pushes, creates the release.
set -euo pipefail
V="${1:?version like 0.3.0}"; NOTE="${2:?one line on what changed}"
cd "$(dirname "$0")/.."
grep -q "## v$V" CHANGELOG.md || { echo "add a '## v$V' section to CHANGELOG.md first"; exit 1; }
grep -rq -E "—|–" skills/remotion-ffmpeg-video && { echo "em or en dash found in the skill; the method bans them"; exit 1; }
python3 - "$V" <<'PY'
import json, sys
p = ".claude-plugin/plugin.json"; d = json.load(open(p)); d["version"] = sys.argv[1]
json.dump(d, open(p, "w"), indent=2); open(p, "a").write("\n")
PY
mkdir -p dist; rm -f dist/remotion-ffmpeg-video.skill
( cd skills && zip -qr ../dist/remotion-ffmpeg-video.skill remotion-ffmpeg-video -x "remotion-ffmpeg-video/evals/*" "*/.DS_Store" "*/__pycache__/*" )
git add -A; git commit -q -m "remotion-ffmpeg-video v$V: $NOTE"
git tag -a "v$V" -m "v$V: $NOTE"; git push -q origin main; git push -q origin "v$V"
gh release create "v$V" dist/remotion-ffmpeg-video.skill --title "remotion-ffmpeg-video v$V" --notes "$NOTE. Full notes in CHANGELOG.md."
echo "released v$V. Students update with: claude plugin marketplace update ashishpunj && claude plugin install remotion-ffmpeg-video@ashishpunj"
