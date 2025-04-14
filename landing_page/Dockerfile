# --- BUILD ---
FROM ghcr.io/ioxiocom/nodejs-base:ubuntu24.04-node22 AS build

WORKDIR /src/landing_page

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
COPY --from=build /src/landing_page/build/ /src/landing_page/build

EXPOSE 8080
