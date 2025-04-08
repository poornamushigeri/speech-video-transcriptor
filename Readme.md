Absolutely! Here's a clean and professional `README.md` that you can **copy-paste directly into your project**:

---

```markdown
# 🎙️ Speech and Video Transcripter & Summariser

An AI-powered Streamlit app that **transcribes** and **summarizes** audio or video files — including **YouTube videos** — using OpenAI Whisper and BART Transformer models.

---
![App Screenshot](app_screenshot.png)


## ✨ Features

- 🎧 Upload audio (`.mp3`, `.wav`) or video (`.mp4`, `.mov`) files
- 🌐 Paste a YouTube link to auto-download and transcribe
- 📝 Generate high-quality transcripts using Whisper
- 🧠 Get concise summaries using BART (facebook/bart-large-cnn)
- 🚀 Streamlit-based clean, interactive UI

---

## 📂 Project Structure

```
.
├── main_app.py              # Streamlit frontend logic
├── processing_utils.py      # Backend processing functions
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Create a virtual environment
```bash
conda create --name venv python=3.10 -y
conda venv mental
```

### 2. 📦 Install dependencies
```bash
pip install -r requirements.txt
```

> ✅ Make sure you have `ffmpeg` installed in your system (it’s used for audio/video processing).  
> [Download FFmpeg](https://ffmpeg.org/download.html)

---

## 🚀 Run the App

### Use this command in your terminal:
```bash
streamlit run main_app.py --browser.gatherUsageStats false
```

The app will open in your default browser at:
```
http://localhost:8501
```

> If it doesn't open automatically, just copy the link above and paste it into any browser.

---

## 🧠 Powered By

- [OpenAI Whisper](https://github.com/openai/whisper) – speech recognition
- [Transformers by Hugging Face](https://huggingface.co/transformers/) – for text summarization
- [Streamlit](https://streamlit.io) – to build the UI
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – to download YouTube videos
- [MoviePy](https://zulko.github.io/moviepy/) + [Pydub](https://github.com/jiaaro/pydub) – for audio/video conversion

---

## 💡 Example Use Cases

- Generate quick meeting or lecture summaries  
- Transcribe interviews and podcasts  
- Understand YouTube videos without watching them fully

---

## 📌 Note

- The summarizer truncates input to 1024 tokens for processing.
- Whisper `base` model is used for better transcription accuracy.

---
