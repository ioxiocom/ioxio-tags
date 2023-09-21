# IOXIO Tags demo

Prerequisites:

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Node 18+ LTS](https://nodejs.org/en/)
- [pnpm](https://pnpm.io/installation)
- [pre-commit](https://pre-commit.com/#install)

If you plan on contributing to the repository, after checking out the repository ensure you run
`pre-commit install` in the repo root.

## Development

### API

```shell
cd api
poetry install
poetry run dev
```

Will by default listen to port 8081.

To sync the FastAPI route definitions to `openapi.ts` -files, run `pre-commit run --all-files` at
the root of the project.

### Generator

```shell
cd generator
pnpm run dev
```

Testing Docker image:

```shell
cd generator
docker build . -t generator
docker run --rm -p 8080:8080 -it generator
```

### Scanner

```shell
cd generator
pnpm run dev
```

Testing Docker image:

```shell
cd scanner
docker build . -t scanner
docker run --rm -p 8080:8080 -it scanner
```
