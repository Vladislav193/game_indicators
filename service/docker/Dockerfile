FROM python:3.10-slim
WORKDIR /app
COPY ../game_indicators .
COPY ../service/celery .
COPY ../requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]