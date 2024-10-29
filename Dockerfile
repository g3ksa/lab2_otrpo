FROM python:3.10-slim

RUN apt-get update

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir opencv-python-headless

CMD ["python", "main.py"]
