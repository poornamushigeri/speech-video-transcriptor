FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg git && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir openai-whisper

EXPOSE 10000

CMD streamlit run main_app.py --server.port=$PORT --server.address=0.0.0.0
