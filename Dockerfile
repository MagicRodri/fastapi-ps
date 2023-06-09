# Base image
FROM python:3.10-slim-bullseye

# Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Work directory
WORKDIR /backend

# Dependencies
COPY ./requirements.txt .
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libavcodec-extra
RUN pip install -r requirements.txt

# Copy project
COPY . .