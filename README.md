# YouTube Urdu Transcriber

Transcribes Urdu-first YouTube speeches (with English mix) into clean Word documents using local AI.

---

## ✨ Features

* Urdu-first transcription (no forced translation)
* Handles Urdu + English mixed speech
* Outputs formatted Word (.docx)
* Progress tracking with time estimation
* Fully local (no API required)

---

## ❓ Why this tool?

Most transcription tools:

* Translate Urdu → English ❌
* Lose original speech structure ❌
* YouTube transcripts render Urdu incorrectly (e.g., as Hindi/Sanskrit text) ❌

This tool preserves:

* Original Urdu language
* Original English phrases
* Natural spoken flow

---

## ⚙️ Installation

### 1. Install Python

Install Python 3.10 or later.

### 2. Install FFmpeg

Download and install FFmpeg, then add it to your system PATH.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script:

```bash
python youtube_urdu_transcriber.py
```

Paste your YouTube link when prompted.

---

## 📄 Output

* Audio file saved locally
* Word document (.docx) transcript (Urdu + English mixed)

---

## 🧠 Optional (Recommended): Improve Paragraphs

For better formatting, use DeepSeek:

Paste your transcriptin DeepSeek and use this prompt:

```
Create clear paragraphs from this text.
Do not reduce content.
Improve words to express context.
Continue with Urdu and English flow of content.
Improve formatting.
```

Then copy the result into Word for a refined transcript.
