FROM python:3.12-slim

WORKDIR /monolith

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY monolith/ .

CMD ["celery", "-A", "app.tasks.celery_app", "worker", "--loglevel=info"]
