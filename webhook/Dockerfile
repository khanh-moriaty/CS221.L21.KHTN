FROM    ubuntu:latest

ARG     DEBIAN_FRONTEND=noninteractive

COPY    ./ src/
WORKDIR src/

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
ENV     FLASK_APP=server.py

RUN     apt-get update; \
        apt-get install -y build-essential; \
        apt-get install -y software-properties-common; \
        apt-get install -y curl; \
        yes | add-apt-repository ppa:deadsnakes/ppa; \
        apt-get update; \
        apt-get install -y python3.6; \
        apt-get install -y python3-distutils; \
        apt-get install -y python3.6-dev; \
        (curl https://bootstrap.pypa.io/get-pip.py | python3.6); \
        python3.6 -m pip install flask;


CMD     flask run -p 7777

