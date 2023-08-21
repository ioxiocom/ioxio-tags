FROM ghcr.io/ioxiocom/nodejs-base:ubuntu22.04-node18 AS runtime

WORKDIR /src/scanner

ADD package.json pnpm-lock.yaml ./
RUN : \
 && set -exu \
 && pnpm install --frozen-lockfile \
 && :

ADD . ./

RUN : \
  && set -exu \
  && pnpm run build \
  && :

ADD docker/runtime-entrypoint.sh ./docker/runtime-entrypoint.sh

USER ${USER}
EXPOSE 8080
ENTRYPOINT ["bash", "/src/scanner/docker/runtime-entrypoint.sh"]
