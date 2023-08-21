#!/usr/bin/env bash

# shellcheck disable=SC2039
set -euo pipefail

if [ "${LOG_LEVEL:-}" = "DEBUG" ]; then
  set -x
fi

# Using PORT if defined (in Google Cloud Run), defaulting to 8080
export PORT=${PORT:-8080}

cd /src/
exec multi-start \
    --frontend \
    --frontend-dir scanner \
    --frontend-cmd "bash -c read -- -p 'No entrypoint configured yet because there is no server set up in this project'" \
    --frontend-port "${PORT}" \
    --service-wait-time 10
