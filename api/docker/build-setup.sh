#!/usr/bin/env bash
#
# WARNING!
# ========
#
# THIS FILE IS NOT USED IN RUNTIME, ONLY WHILE BUILDING DOCKER IMAGES
# DO NOT ADD ANYTHING RUNTIME OR ENVIRONMENT SPECIFIC HERE
#

# shellcheck disable=SC2039
set -exuo pipefail

# Don't install "app" package during this phase, cause the source code is not copied yet
sed -i 's/^packages =.*$//g' /src/api/pyproject.toml

# Allow ${USER} to install python dependencies
chown -R "${USER}":"${GROUP}" /src

su "${USER}" -c ". ${POETRY_HOME}/env; poetry install --no-dev"
