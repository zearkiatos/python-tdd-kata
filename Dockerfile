FROM python:alpine3.9

COPY . /app/

WORKDIR /app

RUN apk add g++ jpeg-dev zlib-dev libjpeg make

RUN make run-tests