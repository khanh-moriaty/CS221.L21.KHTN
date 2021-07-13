FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
ENV     FLASK_APP=server.py FLASK_RUN_PORT=7777

COPY    ./requirements.txt ./
RUN     apt-get update && \
        apt-get install -y wget && \
        wget -q https://thiaisotajppub.s3-ap-northeast-1.amazonaws.com/publicfiles/wiki.vi.model.bin.gz && \
        gzip -d wiki.vi.model.bin.gz && \
        pip install -r requirements.txt

COPY    ./ src/
WORKDIR src/

RUN     mv /wiki.vi.model.bin /src/nlu/

CMD     flask run -h 0.0.0.0

