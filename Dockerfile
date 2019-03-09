FROM python:3-slim

RUN apt-get update &&\
    apt-get install --no-install-recommends -qy \
        build-essential \
        zlib1g-dev \
        libjpeg-dev \
        librsvg2-bin &&\
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip3 install spidev pillow rpi.gpio

WORKDIR /app

ADD . /app
