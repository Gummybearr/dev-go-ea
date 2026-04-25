#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parent
SCRIPT_PATH = ROOT / "part-1-week-1-day-1-audio-script.txt"
OUT_DIR = Path("/tmp/ea_part_1_week_1_day_1_openai_tts_chunks")
WAV_OUT = ROOT / "part-1-week-1-day-1-deep-dive-openai.wav"
M4A_OUT = ROOT / "part-1-week-1-day-1-deep-dive.m4a"
ENV_PATH = Path("/Users/gyunghoe/wesley-07252025/.env.local")


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def split_long_block(block: str, max_chars: int) -> list[str]:
    if len(block) <= max_chars:
        return [block]
    sentences = re.split(r"(?<=[.!?。])\s+", block)
    pieces: list[str] = []
    current = ""
    for sentence in sentences:
        if not current:
            current = sentence
        elif len(current) + 1 + len(sentence) <= max_chars:
            current += " " + sentence
        else:
            pieces.append(current.strip())
            current = sentence
    if current:
        pieces.append(current.strip())
    return pieces


def read_chunks(script: str, max_chars: int = 900) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in script.splitlines():
        if line.startswith("CHUNK "):
            if current:
                paragraphs.append("\n".join(current).strip())
                current = []
            continue
        if not line.strip():
            if current:
                paragraphs.append("\n".join(current).strip())
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append("\n".join(current).strip())

    split_paragraphs: list[str] = []
    for paragraph in paragraphs:
        split_paragraphs.extend(split_long_block(paragraph, max_chars))

    chunks: list[str] = []
    current_chunk = ""
    for paragraph in split_paragraphs:
        if not current_chunk:
            current_chunk = paragraph
        elif len(current_chunk) + 2 + len(paragraph) <= max_chars:
            current_chunk += "\n\n" + paragraph
        else:
            chunks.append(current_chunk)
            current_chunk = paragraph
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def concat_audio(files: list[Path], output: Path) -> None:
    inputs: list[str] = []
    filter_inputs: list[str] = []
    for index, path in enumerate(files):
        inputs.extend(["-i", str(path)])
        filter_inputs.append(f"[{index}:a]")
    filter_complex = "".join(filter_inputs) + f"concat=n={len(files)}:v=0:a=1[a]"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            filter_complex,
            "-map",
            "[a]",
            str(output),
        ],
        check=True,
    )


def main() -> int:
    load_env(ENV_PATH)
    if "OPENAI_API_KEY" not in os.environ:
        raise RuntimeError("Missing OPENAI_API_KEY")

    chunks = read_chunks(SCRIPT_PATH.read_text(), max_chars=900)

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(exist_ok=True)

    client = OpenAI(timeout=120.0, max_retries=2)
    chunk_files: list[Path] = []
    instructions = (
        "Speak as a calm, natural Korean study tutor. Keep English tax terms in English, "
        "pronouncing acronyms clearly but not robotically. Use a measured audiobook pace, "
        "with short pauses between ideas. Do not add extra content."
    )

    for index, chunk in enumerate(chunks, start=1):
        path = OUT_DIR / f"part-1-week-1-day-1-deep-dive-{index:02d}.wav"
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="marin",
            input=chunk,
            instructions=instructions,
            response_format="wav",
        ) as response:
            response.stream_to_file(path)
        chunk_files.append(path)
        print(f"Wrote {path}")

    concat_audio(chunk_files, WAV_OUT)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(WAV_OUT),
            "-codec:a",
            "aac",
            "-b:a",
            "96k",
            str(M4A_OUT),
        ],
        check=True,
    )
    print(f"Wrote {WAV_OUT}")
    print(f"Wrote {M4A_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
