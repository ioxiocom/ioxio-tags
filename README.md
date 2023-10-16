# IOXIO Tags™️ demo

Demonstrating usage of [IOXIO](https://ioxio.com) Tags™️, using QR Codes to connect real world goods
to data products on Dataspaces™.

Provides some basic scaffolding demonstrating:

- How to generate IOXIO Tags™️ -compatible codes, both [COSE](https://cose-wg.github.io/cose-spec/)
  signed and simple URL -types.
- How to generate a valid signing key and publish it via JWKS.
- How to verify COSE signed IOXIO Tags™️ via JWKS
- How to host the metadata for your domain and products you will issue IOXIO Tags™️ for.
- How to fetch the relevant metadata from issuer servers
- How to fetch data products according to the Digital Product Passport -compatible data product
  definition standards from an IOXIO Dataspace™️

Demo environment deployed to [tags.ioxio.dev](https://tags.ioxio.dev), but for properly testing the
capabilities out for use in your own organization you will want to run the demo components on your
own. Otherwise you cannot e.g. make valid COSE signatures for your own domain.

Prerequisites:

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Node 18+ LTS](https://nodejs.org/en/)
- [pnpm](https://pnpm.io/installation)

If you plan on contributing to the repository ensure you install
[pre-commit](https://pre-commit.com/#install) , and after checking out the repository ensure you run
`pre-commit install` in the repo root.

For testing you should first set up the `api`, then run `generator` and generate QR codes - we
suggest printing them at 5x5cm size for easier testing, then run the `scanner`. Using a USB web
camera will make testing the actual scanning easier.

## Development

### API

```shell
cd api
poetry install
poetry run dev
```

Will by default listen to port 8081, and will likely fail by default. Read
[api/README.md](api/README.md) for details.

To sync the FastAPI route definitions to `openapi.ts` -files, run `pre-commit run --all-files` at
the root of the project.

### Generator

```shell
cd generator
pnpm run dev
```

### Scanner

```shell
cd scanner
pnpm run dev
```
