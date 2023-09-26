#!/usr/bin/env bash

# shellcheck disable=SC2039
set -euo pipefail

if [ "${LOG_LEVEL:-}" = "DEBUG" ]; then
  set -x
fi

# Works even when mounted on Windows
export INVOKE_RUN_SHELL="/bin/sh"

# Using PORT if defined (in Google Cloud Run), defaulting to 8080
export PORT=${PORT:-8080}

cd api
poetry run serve
