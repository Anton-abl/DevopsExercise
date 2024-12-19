# Stage 1
FROM python:3.11-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

COPY cat-app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --target /app/venv

#Stage 2
FROM python:3.11-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache libffi

WORKDIR /app

COPY --from=builder /app/venv /app/venv

ENV PYTHONPATH=/app/venv

COPY cat-app/CatScript.py .

EXPOSE 5000

CMD ["python", "CatScript.py"]
