```markdown
# 🎙️ Speech and Video Transcripter & Summariser

An AI-powered Streamlit app that **transcribes** and **summarizes** audio or video files — including **YouTube videos** — using OpenAI Whisper and BART Transformer models.

<p align="center">
  <img src="app_screenshot.png" alt="App Screenshot" width="700"/>
</p>

---

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
├── screenshot.png           # App preview image
├── example_output.png       # Example transcript/summary output
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Create a virtual environment
```bash
conda create --name mental python=3.10 -y
conda activate mental
```

### 2. 📦 Install dependencies
```bash
pip install -r requirements.txt
```

> ✅ Make sure you have `ffmpeg` installed in your system (it’s used for audio/video processing).  
> [Download FFmpeg](https://ffmpeg.org/download.html)

---

## 🚀 Run the App

```bash
streamlit run main_app.py
```

The app will open in your default browser at:
```
http://localhost:8501
```

> If it doesn't open automatically, copy the link above and paste it into your browser.

---

## 🧪 Example Output

Below is an example of how the app displays the generated transcript and summary after uploading a file or pasting a YouTube link.

<p align="center">
  <img src="example_output.png" alt="Transcript and Summary Output" width="700"/>
</p>

---

## 🧠 Powered By

- OpenAI Whisper – speech recognition  
- Hugging Face Transformers – for text summarization  
- Streamlit – to build the UI  
- yt-dlp – to download YouTube videos  
- MoviePy + Pydub – for audio/video conversion  

---

## 💡 Example Use Cases

- Generate quick meeting or lecture summaries  
- Transcribe interviews and podcasts  
- Understand YouTube videos without watching them fully  

---

## 📌 Notes

- The summarizer truncates input to 1024 tokens for processing  
- Whisper `base` model is used for better transcription accuracy
```