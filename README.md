# IOXIO Tags demo

Prerequisites:

- [Node 18+ LTS](https://nodejs.org/en/)
- [pnpm](https://pnpm.io/installation)
- [pre-commit](https://pre-commit.com/#install)

If you plan on contributing to the repository, after checking out the repository ensure you run
`pre-commit install` in the repo root.

## Development

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
