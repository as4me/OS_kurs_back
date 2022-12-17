FROM python:latest as img1

WORKDIR /usr/app/src



COPY server_1.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM python:latest as img2
WORKDIR /usr/app/src




COPY server_2.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt