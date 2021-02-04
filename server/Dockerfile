FROM python:3.8-slim

ENV TZ Europe/Moscow
ENV PYTHONDONTWRITEBYTECODE yes

RUN mkdir /app
ENV HOME=/app
ENV PYTHONPATH=$HOME
WORKDIR $HOME

RUN apt-get update && apt-get install -y curl libmagic-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY testmotmom $HOME/testmotmom
COPY migrations $HOME/migrations
COPY alembic.ini $HOME/alembic.ini