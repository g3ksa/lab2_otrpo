# Face Detection Application

Это приложение на Python использует библиотеку OpenCV для распознавания лиц на изображении. Оно запускается в Docker-контейнере и автоматически публикуется в DockerHub с использованием GitHub Actions.

## Описание

Приложение загружает изображение `image1.jpg`, расположенное в корневой директории проекта, и использует каскад Хаара для обнаружения лиц. Результаты координат найденных лиц выводятся в `stdout`.

## Установка и запуск

```bash
git clone https://github.com/g3ksa/lab2_otrpo.git
cd face-detection-app
```

### Локальный запуск

```bash
pip install opencv-python-headless
python main.py
```

### Локальный запуск в docker (локальная сборка)
```bash
docker build -t face-detection-app .
docker run --rm face-detection-app
```

### Локальный запуск в docker (образ с dockerhub)
```bash
docker run --rm akuzm1n/opencv-face-detection:latest
```
