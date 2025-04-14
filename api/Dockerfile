# ----- Server build ----- #

FROM ghcr.io/ioxiocom/python-base:ubuntu24.04-python3.13 AS api

WORKDIR /src/api

ADD docker/build-prepare.sh docker/
RUN bash docker/build-prepare.sh

ADD docker/build-setup.sh docker/
ADD pyproject.toml poetry.lock ./

RUN bash docker/build-setup.sh


# ----- Runtime environment ----- #

FROM ghcr.io/ioxiocom/python-base:ubuntu24.04-python3.13 AS runtime

# Copy results from build environments
COPY --from=api ${WORKON_HOME} ${WORKON_HOME}

# Copy some scripts over
WORKDIR /src
ADD docker/runtime-prepare.sh api/docker/

# Copy all the api code over
ADD . api/

# Prepare runtime
RUN : \
    && set -exu \
    && bash /src/api/docker/runtime-prepare.sh \
    && python -m compileall . \
    && :

ADD docker/runtime-entrypoint.sh api/docker/

USER ${USER}
EXPOSE 8080
ENTRYPOINT ["bash", "/src/api/docker/runtime-entrypoint.sh"]
