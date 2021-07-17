FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

RUN     apt-get update && \
        apt-get install -y build-essential && \
        pip install gdown && \
        gdown --id 1eK0BuKOMtqOYnZ45cPfXm9WRbkR-iX80

COPY    ./requirements.txt ./
RUN     pip install -r requirements.txt

COPY    ./ src/
WORKDIR src/

# CMD     flask run -h 0.0.0.0
CMD     gunicorn --bind 0.0.0.0:7777 -k gevent --worker-connections 1000 server:app