FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
ENV     FLASK_APP=server.py FLASK_RUN_PORT=7777

COPY    ./requirements.txt ./
RUN     apt-get update && \
        apt-get install -y build-essential && \
        pip install -r requirements.txt && \
        gdown --id 1eK0BuKOMtqOYnZ45cPfXm9WRbkR-iX80

COPY    ./ src/
WORKDIR src/

CMD     flask run -h 0.0.0.0

