#!/usr/bin/env bash
#
# This step is for initializing the runtime environment
#

# shellcheck disable=SC2039
set -exuo pipefail

# Set up PYTHONPATH for the main package. Only this module will be installed
cd /src/api
su "${USER}" -c ". ${POETRY_HOME}/env; poetry install --no-dev"

apt-get update
apt-get install -y --no-install-recommends \
        libcairo2 \
        libcairo2-dev \
        # Intentionally left blank
# Ensure user cannot edit the filesystem contents
chown -R root:root .
