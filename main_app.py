import streamlit as st
from processing_utils import extract_audio_from_video, convert_audio, transcribe_audio, summarize_text
import os
import time
import subprocess
from pathlib import Path
from uuid import uuid4

st.set_page_config(page_title="Speech Transcripter", layout="centered", page_icon="🎧")

if "loaded" not in st.session_state:
    with st.spinner("🔄 Loading Speech and Video Transcripter & Summariser..."):
        time.sleep(1.5)
    st.session_state.loaded = True

st.title("🎙 Speech and Video Transcripter & Summariser")
st.markdown(
    "Upload an *audio* or *video* file or paste a *YouTube link* to generate an AI-powered *transcript and summary*."
)

tab1, tab2 = st.tabs(["📤 Upload File", "🌐 Paste YouTube Link"])

video_path = None

with tab1:
    uploaded_file = st.file_uploader("Choose audio/video file", type=["mp3", "wav", "mp4", "mov"])
    if uploaded_file:
        ext = uploaded_file.name.split(".")[-1]
        temp_filename = f"temp_input.{ext}"
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.read())
        video_path = temp_filename

with tab2:
    youtube_url = st.text_input("Paste YouTube video link here")
    if youtube_url:
        video_id = str(uuid4())[:8]
        temp_filename = f"yt_video_{video_id}.mp4"
        with st.spinner("⬇ Downloading video..."):
            try:
                result = subprocess.run(
                    ["yt-dlp", "-f", "mp4", "-o", temp_filename, youtube_url],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0 and Path(temp_filename).exists():
                    video_path = temp_filename
                else:
                    st.error("⚠ Failed to download video. Please check the link or try another one.")
            except Exception as e:
                st.error(f"⚠ Exception: {e}")

# ---- Processing ----
if video_path:
    with st.status("Processing file...", expanded=True) as status:
        converted_audio = "converted.wav"
        st.write("🔄 Extracting/converting audio...")
        if video_path.endswith((".mp4", ".mov")):
            extract_audio_from_video(video_path, converted_audio)
        else:
            convert_audio(video_path, converted_audio)

        st.write("📝 Transcribing audio...")
        transcript = transcribe_audio(converted_audio)

        st.write("🧠 Summarizing text...")
        summary = summarize_text(transcript)

        status.update(label="✅ All done!", state="complete", expanded=False)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Transcript")
        st.text_area("Full Transcript", transcript, height=300)

    with col2:
        st.subheader("🧠 Summary")
        st.text_area("Summary", summary, height=300)

    st.success("🎉 Done! You can upload a new file or paste another video link.")

    os.remove(video_path)
    os.remove(converted_audio)