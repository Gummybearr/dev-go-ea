#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
import time
import wave
from pathlib import Path

from google import genai
from google.genai import types


ROOT = Path(__file__).resolve().parent
MASTERCLASS_DIR = ROOT / "week1-day2-masterclass"
OUT_DIR = Path("/tmp/ea_week1_day2_gemini_tts_chunks")
ENV_PATHS = [
    Path("/Users/gyunghoe/wesley-07252025/.env.val"),
    Path("/Users/gyunghoe/wesley-07252025/.env.local"),
]
MODEL = "gemini-2.5-flash-preview-tts"
VOICE_NAME = "Sadaltager"


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


def write_wave(path: Path, pcm: bytes, channels: int = 1, rate: int = 24000, sample_width: int = 2) -> None:
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)


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
            "-hide_banner",
            "-loglevel",
            "error",
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


def make_prompt(chunk: str) -> str:
    return f"""
# AUDIO PROFILE
Korean EA exam master instructor. The voice is knowledgeable, warm, and confident.

## DIRECTOR'S NOTES
Speak naturally in Korean, like a premium recorded tax exam lecture.
Keep English tax terms in English.
Pronounce acronyms such as MFJ, MFS, HOH, QSS, IRS, and SEE clearly.
Use a calm but engaging pace, with short pauses between ideas.
Do not add extra content.
Read only the transcript after the TRANSCRIPT heading.

## TRANSCRIPT
{chunk}
""".strip()


def generate_chunk(client: genai.Client, chunk: str) -> bytes:
    response = client.models.generate_content(
        model=MODEL,
        contents=make_prompt(chunk),
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=VOICE_NAME,
                    )
                )
            ),
        ),
    )
    try:
        data = response.candidates[0].content.parts[0].inline_data.data
    except Exception as exc:
        raise RuntimeError(f"Gemini TTS response did not contain audio: {response!r}") from exc
    if not isinstance(data, bytes):
        raise TypeError(f"Expected bytes audio data, got {type(data).__name__}")
    return data


def render_script(client: genai.Client, script_path: Path) -> None:
    slug = script_path.name.removesuffix("-audio-script.txt")
    module_dir = OUT_DIR / slug
    wav_out = module_dir / f"{slug}.wav"
    m4a_out = MASTERCLASS_DIR / f"{slug}.m4a"

    if module_dir.exists():
        shutil.rmtree(module_dir)
    module_dir.mkdir(parents=True, exist_ok=True)

    chunks = read_chunks(script_path.read_text(encoding="utf-8"), max_chars=900)
    chunk_files: list[Path] = []
    for index, chunk in enumerate(chunks, start=1):
        path = module_dir / f"{slug}-{index:02d}.wav"
        last_error: Exception | None = None
        for attempt in range(1, 4):
            try:
                pcm = generate_chunk(client, chunk)
                write_wave(path, pcm)
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                if attempt < 3:
                    time.sleep(3 * attempt)
        if last_error is not None:
            raise last_error
        chunk_files.append(path)
        print(f"Wrote {path}", flush=True)

    concat_audio(chunk_files, wav_out)
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(wav_out),
            "-codec:a",
            "aac",
            "-b:a",
            "96k",
            str(m4a_out),
        ],
        check=True,
    )
    print(f"Wrote {m4a_out}", flush=True)


def main() -> int:
    for env_path in ENV_PATHS:
        load_env(env_path)

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY or GOOGLE_GENERATIVE_AI_API_KEY")

    scripts = sorted(MASTERCLASS_DIR.glob("*-audio-script.txt"))
    if not scripts:
        raise RuntimeError(f"No audio scripts found in {MASTERCLASS_DIR}")

    client = genai.Client(api_key=api_key)
    for script_path in scripts:
        render_script(client, script_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
