FROM    node:16-buster-slim

ARG     FRONTEND_DOMAIN=.

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8

RUN     npm install -g serve

COPY    ./ src/
WORKDIR src/

RUN     sed -E "s,^( *\"homepage\": *)(\")(.*)(\".*)$,\1\2${FRONTEND_DOMAIN}\4," -i package.json; \
        yarn install; \
        yarn build;

CMD     serve -s build -l 3000