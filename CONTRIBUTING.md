# Contributing to YouTube Urdu Transcriber

Thank you for your interest in contributing! This guide will help you get started quickly.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Setting Up the Project](#setting-up-the-project)
- [How to Contribute](#how-to-contribute)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Contribution Ideas](#contribution-ideas)
- [Code Style Guidelines](#code-style-guidelines)

---

## Getting Started

Before contributing, make sure you have the following installed:

- Python 3.10 or later → [Download](https://www.python.org/downloads/)
- Git → [Download](https://git-scm.com/downloads)
- FFmpeg → [Download](https://ffmpeg.org/download.html) *(add it to your system PATH)*

---

## Setting Up the Project

### 1. Fork the Repository

Click the **Fork** button at the top right of the [repository page](https://github.com/DrArifAlvi/youtube-urdu-transcriber) to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/youtube-urdu-transcriber.git
cd youtube-urdu-transcriber
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `faster-whisper` — local AI transcription model
- `yt-dlp` — YouTube audio downloader
- `python-docx` — Word document generation
- `tqdm` — progress bar
- `regex` — text processing

### 4. Run the Tool to Verify Setup

```bash
python youtube_urdu_transcriber.py
```

Paste a YouTube URL when prompted. If a `.docx` file is generated, your setup is working correctly.

---

## How to Contribute

### Step 1 — Create a New Branch

Always create a separate branch for your work. Never commit directly to `main`.

```bash
git checkout -b your-feature-name
```

Examples:
```bash
git checkout -b add-batch-processing
git checkout -b fix-ffmpeg-error-message
git checkout -b improve-readme
```

### Step 2 — Make Your Changes

Edit or add files as needed. Keep your changes focused — one feature or fix per branch.

### Step 3 — Commit Your Changes

```bash
git add .
git commit -m "Brief description of what you changed"
```

Good commit message examples:
- `Add batch URL processing support`
- `Fix crash when FFmpeg is not in PATH`
- `Add output directory flag to CLI`

### Step 4 — Push to Your Fork

```bash
git push origin your-feature-name
```

---

## Submitting a Pull Request

1. Go to your fork on GitHub
2. Click **"Compare & pull request"**
3. Write a clear title and description explaining:
   - What you changed
   - Why you made the change
   - How to test it (if code was changed)
4. Click **"Create pull request"**

The maintainer will review and merge it if everything looks good. 🎉

---

## Contribution Ideas

Not sure where to start? Here are some ideas:

| Difficulty | Idea |
|------------|------|
| ⭐ Beginner | Improve README with badges or screenshots |
| ⭐ Beginner | Add more descriptive error messages |
| ⭐⭐ Intermediate | Add `--output-dir` CLI argument to choose save location |
| ⭐⭐ Intermediate | Support batch processing of multiple YouTube URLs |
| ⭐⭐ Intermediate | Add a simple Streamlit or Tkinter GUI |
| ⭐⭐⭐ Advanced | Add speaker diarization (detect multiple speakers) |
| ⭐⭐⭐ Advanced | Add GitHub Actions workflow for linting |

Feel free to open an **Issue** first to discuss your idea before building it.

---

## Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) Python style conventions
- Use descriptive variable names (avoid single letters like `x`, `d`)
- Add comments for any non-obvious logic
- Keep functions small and focused on one task

---

## Questions?

Open an [Issue](https://github.com/DrArifAlvi/youtube-urdu-transcriber/issues) and the maintainer or community will help you out.

Happy contributing! 🚀
