FROM python:latest

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


COPY ./server_1.py /app/server_1.py
COPY ./server_2.py /app/server_2.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt




