FROM    node:16-buster-slim

COPY    ./ src/
WORKDIR src/

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8

RUN     yarn install

CMD     yarn start