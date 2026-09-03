#!/usr/bin/env python3
"""Create a safe, machine-readable ffprobe/decode receipt for one local media file."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def _run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=False, capture_output=True, text=True)


def _tool_version(binary: str) -> str:
    result = _run([binary, "-version"])
    if result.returncode != 0:
        return "unknown"
    return result.stdout.splitlines()[0] if result.stdout else "unknown"


def _number(value: Any) -> float | None:
    if value in (None, "", "N/A"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _fps(value: Any) -> float | None:
    if value in (None, "", "0/0", "N/A"):
        return None
    try:
        return float(Fraction(str(value)))
    except (ValueError, ZeroDivisionError):
        return None


def _rotation(stream: dict[str, Any]) -> int | None:
    tags = stream.get("tags") or {}
    tagged = tags.get("rotate")
    if tagged not in (None, ""):
        try:
            return int(round(float(tagged)))
        except (TypeError, ValueError):
            pass
    for item in stream.get("side_data_list") or []:
        value = item.get("rotation")
        if value is not None:
            try:
                return int(round(float(value)))
            except (TypeError, ValueError):
                continue
    return None


def _stream_summary(stream: dict[str, Any]) -> dict[str, Any]:
    return {
        "index": stream.get("index"),
        "type": stream.get("codec_type"),
        "codec": stream.get("codec_name"),
        "profile": stream.get("profile"),
        "width": stream.get("width"),
        "height": stream.get("height"),
        "sample_aspect_ratio": stream.get("sample_aspect_ratio"),
        "display_aspect_ratio": stream.get("display_aspect_ratio"),
        "pixel_format": stream.get("pix_fmt"),
        "average_frame_rate": stream.get("avg_frame_rate"),
        "average_fps": _fps(stream.get("avg_frame_rate")),
        "real_frame_rate": stream.get("r_frame_rate"),
        "real_fps": _fps(stream.get("r_frame_rate")),
        "time_base": stream.get("time_base"),
        "start_time_seconds": _number(stream.get("start_time")),
        "duration_seconds": _number(stream.get("duration")),
        "frame_count": stream.get("nb_frames"),
        "rotation_degrees": _rotation(stream),
        "colour_range": stream.get("color_range"),
        "colour_space": stream.get("color_space"),
        "colour_transfer": stream.get("color_transfer"),
        "colour_primaries": stream.get("color_primaries"),
        "sample_rate_hz": _number(stream.get("sample_rate")),
        "channels": stream.get("channels"),
        "channel_layout": stream.get("channel_layout"),
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing receipt: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def audit(media: Path, *, decode: bool, include_sha256: bool) -> tuple[dict[str, Any], int]:
    ffprobe = shutil.which("ffprobe")
    ffmpeg = shutil.which("ffmpeg")
    if ffprobe is None:
        raise RuntimeError("ffprobe is not available on PATH")
    if decode and ffmpeg is None:
        raise RuntimeError("ffmpeg is not available on PATH")

    probe_result = _run([
        ffprobe,
        "-v", "error",
        "-show_format",
        "-show_streams",
        "-show_chapters",
        "-of", "json",
        str(media),
    ])
    if probe_result.returncode != 0:
        raise RuntimeError(probe_result.stderr.strip() or "ffprobe failed")

    raw = json.loads(probe_result.stdout)
    summaries = [_stream_summary(row) for row in raw.get("streams") or []]
    first_video = next((row for row in summaries if row["type"] == "video"), None)
    first_audio = next((row for row in summaries if row["type"] == "audio"), None)
    video_duration = first_video and first_video.get("duration_seconds")
    audio_duration = first_audio and first_audio.get("duration_seconds")
    duration_delta = None
    if video_duration is not None and audio_duration is not None:
        duration_delta = abs(video_duration - audio_duration)

    decode_receipt: dict[str, Any] = {"requested": decode, "passed": None, "errors": []}
    exit_code = 0
    if decode:
        assert ffmpeg is not None
        decode_result = _run([
            ffmpeg,
            "-v", "error",
            "-i", str(media),
            "-map", "0:v:0?",
            "-map", "0:a:0?",
            "-f", "null",
            "-",
        ])
        errors = [line for line in decode_result.stderr.splitlines() if line.strip()]
        decode_receipt = {
            "requested": True,
            "passed": decode_result.returncode == 0,
            "errors": errors,
        }
        if decode_result.returncode != 0:
            exit_code = 2

    format_info = raw.get("format") or {}
    payload: dict[str, Any] = {
        "schema_version": 1,
        "status": "PASS" if exit_code == 0 else "FAIL",
        "media": str(media.resolve()),
        "file_size_bytes": media.stat().st_size,
        "sha256": _sha256(media) if include_sha256 else None,
        "tools": {
            "ffprobe": _tool_version(ffprobe),
            "ffmpeg": _tool_version(ffmpeg) if ffmpeg else None,
        },
        "summary": {
            "format_name": format_info.get("format_name"),
            "format_long_name": format_info.get("format_long_name"),
            "start_time_seconds": _number(format_info.get("start_time")),
            "duration_seconds": _number(format_info.get("duration")),
            "bit_rate": _number(format_info.get("bit_rate")),
            "stream_count": len(summaries),
            "video_audio_duration_delta_seconds": duration_delta,
            "streams": summaries,
        },
        "decode": decode_receipt,
        "ffprobe": raw,
    }
    return payload, exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path, help="Local media file to inspect")
    parser.add_argument("--decode", action="store_true", help="Decode the first video/audio streams end to end")
    parser.add_argument("--sha256", action="store_true", help="Hash the full media file")
    parser.add_argument("--output", type=Path, help="Optional JSON receipt path; stdout is always emitted")
    parser.add_argument("--overwrite", action="store_true", help="Allow replacement of an existing receipt")
    args = parser.parse_args()

    media = args.media.expanduser()
    if not media.exists() or not media.is_file():
        print(json.dumps({"status": "ERROR", "error": f"Media file not found: {media}"}), file=sys.stderr)
        return 2

    try:
        payload, exit_code = audit(media, decode=args.decode, include_sha256=args.sha256)
        if args.output:
            _write_json(args.output.expanduser(), payload, args.overwrite)
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return exit_code
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
