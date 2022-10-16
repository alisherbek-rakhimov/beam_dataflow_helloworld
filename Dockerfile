FROM python:3.8.14

WORKDIR /opt/test

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY main.py main.py

RUN python -m pip install --upgrade pip \
    && pip install wheel \
    && pip install apache-beam[gcp] \
    && echo 'MY NAME IS THOMAS SHELBY' > a.txt
