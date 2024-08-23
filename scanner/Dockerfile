# --- BUILD ---
FROM ghcr.io/ioxiocom/nodejs-base:ubuntu22.04-node18@sha256:7ba92e190c476e077c6276b716fbed32b1198dbae0d89e233f3f5c260c4d2c3d AS build

ARG API_BASE_URL="https://api.tags.ioxio.dev"

ENV PUBLIC_API_BASE_URL=$API_BASE_URL
ENV PUBLIC_DEVELOPMENT="false"

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

# --- RUNTIME ---
FROM ghcr.io/ioxiocom/nginx-base AS runtime

ADD nginx/global-security-headers.conf /etc/nginx/global-security-headers.conf
ADD nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# Copy results from build stage
COPY --from=build /src/scanner/build/ /src/scanner/build

EXPOSE 8080
