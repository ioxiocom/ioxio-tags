# ----- React build ----- #

FROM ghcr.io/ioxiocom/nodejs-base:ubuntu24.04-node22 AS frontend

WORKDIR /src/frontend

ADD package.json pnpm-lock.yaml ./
RUN : \
  && set -exu \
  && pnpm install --frozen-lockfile \
  && :

ADD . .

RUN : \
  && set -exu \
  && pnpm run build \
  # Make it possible for runtime to manage its own files
  && chown -R "${USER}:${GROUP}" /src/frontend/.svelte-kit \
  && :

USER ${USER}
EXPOSE 8080
ENTRYPOINT ["bash", "/src/frontend/docker/runtime-entrypoint.sh"]
