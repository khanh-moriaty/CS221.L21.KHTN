FROM    node:16-buster-slim

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8

RUN     npm install -g serve

COPY    ./ src/
WORKDIR src/

RUN     yarn install; \
        yarn build;

CMD     serve -s build -l 3000