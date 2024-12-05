FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install Flask google-cloud-storage

EXPOSE 8080

CMD ["python", "main.py"]
