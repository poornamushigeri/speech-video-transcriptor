# Use a lightweight Python image
FROM python:3.10-slim

# Install system packages (FFmpeg and other essentials)
RUN apt-get update && apt-get install -y ffmpeg git && apt-get clean

# Set working directory
WORKDIR /app

# Copy all project files to container
COPY . .

# Install Python dependencies
# Install openai-whisper correctly (force install from GitHub if needed)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir openai-whisper

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
