FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
ENV     FLASK_APP=server.py FLASK_RUN_PORT=7777

RUN     pip install flask

COPY    ./ src/
WORKDIR src/


CMD     flask run -h 0.0.0.0

