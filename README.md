## Installation

### 1. Install Python

Download and install Python 3.10 or 3.11.

---

### 2. Install FFmpeg

Download FFmpeg from:
https://ffmpeg.org/download.html

After downloading:

* Extract the folder
* Add the `bin` folder to your system PATH

Test installation:

```
ffmpeg -version
```

---

### 3. Install Python Requirements

Open terminal in the project folder and run:

```
pip install -r requirements.txt
```

---

## Usage

Run the script:

```
python youtube_urdu_transcriber.py
```

Paste your YouTube URL when prompted.

---

## Output

* MP3 audio file
* Word (.docx) transcript (in `output/` folder)

---

## Optional and Recommended: Improve Paragraphs with DeepSeek

You can refine formatting using DeepSeek:Copy output and paste in DeepSeek with following directions.

Prompt:

```
Create clear paragraphs from this text.
Make paragraphs.
Do NOT reduce words.
Preserve Urdu and English.
Improve formatting.
```
Copy result you get from DeepSeek in Word