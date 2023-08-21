#!/usr/bin/env bash

# shellcheck disable=SC2039
set -euo pipefail

if [ "${LOG_LEVEL:-}" = "DEBUG" ]; then
  set -x
fi

# Using PORT if defined (in Google Cloud Run), defaulting to 8080
export PORT=${PORT:-8080}

set -- pnpm run start -- --port "${PORT}"
exec "$@"
