import os
import re
import time
import shutil
from datetime import timedelta

import yt_dlp
from faster_whisper import WhisperModel
from docx import Document
from docx.shared import Pt
from tqdm import tqdm

# =======================
# SETTINGS
# =======================
MODEL_SIZE = "large-v3"
DEVICE = "cpu"            # change to "auto" later if needed
COMPUTE_TYPE = "int8"
CPU_THREADS = 8

PAUSE_THRESHOLD = 2.5
EN_WORD_THRESHOLD = 4

# =======================
# PATHS (PORTABLE)
# =======================
BASE_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# =======================
# CHECK FFMPEG
# =======================
def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("\nERROR: FFmpeg not found.\n")
        print("Please install FFmpeg and add it to your system PATH.")
        print("Download from: https://ffmpeg.org/download.html\n")
        exit(1)

# =======================
# DOWNLOAD AUDIO
# =======================
def download_audio(url):
    print("Downloading audio...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    audio_file = os.path.splitext(filename)[0] + ".mp3"
    title = info.get("title", "transcript")

    print(f"Audio saved: {audio_file}")
    return audio_file, title


# =======================
# UTILS
# =======================
def is_english_word(word):
    return re.match(r"^[A-Za-z0-9\-]+$", word) is not None


def split_english_chunks(text):
    words = text.split()
    chunks = []
    current = []
    current_type = None

    for w in words:
        is_eng = is_english_word(w)

        if current_type is None:
            current_type = is_eng
            current.append(w)
        elif is_eng == current_type:
            current.append(w)
        else:
            chunks.append((current_type, current))
            current = [w]
            current_type = is_eng

    if current:
        chunks.append((current_type, current))

    return chunks


def apply_english_rule(text):
    chunks = split_english_chunks(text)
    parts = []

    for is_eng, words in chunks:
        if is_eng and len(words) >= EN_WORD_THRESHOLD:
            parts.append("\n" + " ".join(words))
        else:
            parts.append(" ".join(words))

    return " ".join(parts)


def deduplicate_lines(lines):
    cleaned = []
    prev = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.lower() == prev.lower():
            continue

        cleaned.append(line)
        prev = line

    return cleaned


# =======================
# TRANSCRIPTION
# =======================
def transcribe(audio_file):
    print(f"Loading model: {MODEL_SIZE}")

    model = WhisperModel(
        MODEL_SIZE,
        device=DEVICE,
        compute_type=COMPUTE_TYPE,
        cpu_threads=CPU_THREADS
    )

    segments, info = model.transcribe(
        audio_file,
        beam_size=5,
        language="ur",
        task="transcribe"
    )

    segments = list(segments)

    total_duration = info.duration
    start_time = time.time()

    print("\nTranscribing...\n")

    processed = []
    last_percent = -1

    for seg in tqdm(segments, desc="Processing"):
        processed.append(seg)

        progress = seg.end / total_duration if total_duration else 0
        percent = int(progress * 100)

        if percent != last_percent:
            elapsed = time.time() - start_time
            eta = (elapsed / progress - elapsed) if progress > 0 else 0

            print(f"{percent}% done | ETA: {timedelta(seconds=int(eta))}")
            last_percent = percent

    print("Transcription complete.")
    return processed


# =======================
# PARAGRAPHS
# =======================
def build_paragraphs(segments):
    paragraphs = []
    current = ""
    last_end = 0.0

    for seg in segments:
        text = seg.text.strip()
        if not text:
            continue

        gap = seg.start - last_end

        if gap > PAUSE_THRESHOLD and current:
            paragraphs.append(current.strip())
            current = ""

        current += " " + text
        last_end = seg.end

    if current:
        paragraphs.append(current.strip())

    return paragraphs


# =======================
# SAVE DOCX
# =======================
def save_docx(paragraphs, title):
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
    output_path = os.path.join(OUTPUT_DIR, f"{safe_title}.docx")

    doc = Document()
    doc.add_heading(safe_title, 0)

    for para in paragraphs:
        para = apply_english_rule(para)

        lines = para.split("\n")
        lines = deduplicate_lines(lines)

        final_para = "\n".join(lines)

        p = doc.add_paragraph(final_para)

        for run in p.runs:
            run.font.name = "Segoe UI"
            run.font.size = Pt(12)

    doc.save(output_path)

    print(f"\nSaved: {output_path}")


# =======================
# MAIN
# =======================
def main():
    check_ffmpeg()

    url = input("Enter YouTube URL: ").strip()

    if not url:
        print("No URL provided.")
        return

    audio_file, title = download_audio(url)

    segments = transcribe(audio_file)

    paragraphs = build_paragraphs(segments)

    save_docx(paragraphs, title)


if __name__ == "__main__":
    main()