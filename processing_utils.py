from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from transformers import pipeline
import whisper
import os

# Use BART large CNN for better quality
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_audio_from_video(video_path, output_wav_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile("temp_audio.mp3")
    audio = AudioSegment.from_file("temp_audio.mp3")
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_wav_path, format="wav")
    os.remove("temp_audio.mp3")

def convert_audio(audio_path, output_wav_path):
    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_wav_path, format="wav")

def transcribe_audio(audio_path):
    model = whisper.load_model("tiny")  # fast transcription
    result = model.transcribe(audio_path)
    return result['text']

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary