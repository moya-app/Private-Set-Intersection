FROM python:3.12.13-slim-trixie

RUN pip install uv

WORKDIR /app

RUN apt update && apt install -y --no-install-recommends g++ libgmp3-dev

COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

COPY . .
