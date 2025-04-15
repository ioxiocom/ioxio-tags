# IOXIO Tags™ demo

Demonstrating usage of [IOXIO](https://ioxio.com) Tags™, using QR Codes to connect real world goods
to data products on Dataspaces™.

Provides some basic scaffolding demonstrating:

- How to generate IOXIO Tags™ -compatible codes, both [COSE](https://cose-wg.github.io/cose-spec/)
  signed and simple URL -types.
- How to generate a valid signing key and publish it via JWKS.
- How to verify COSE signed IOXIO Tags™ via JWKS.
- How to host the metadata for your domain and products you will issue IOXIO Tags™ for.
- How to fetch the relevant metadata from issuer servers.
- How to fetch data products according to the Digital Product Passport -compatible data product
  definition standards from an IOXIO Dataspace™.

Demo environment deployed to [tags.ioxio.dev](https://tags.ioxio.dev), but for properly testing the
capabilities out for use in your own organization you will want to run the demo components on your
own. Otherwise you cannot e.g. make valid COSE signatures for your own domain.

Technical documentation on creating and using IOXIO Tags™ is available at
[docs.ioxio.dev/tags/](https://docs.ioxio.dev/tags/)

## Demo data

To publish more demo products or modify the demo data, you should look at the following:

- [./demo_data](./demo_data) - Hosts public files, product metadata, and images. New product types
  need a new file in
  [.well-known/product-passport/products/{product}.json](./demo_data/.well-known/product-passport/products/).
  The filename without extension needs to match the value of the `product` field in the code.
- [./generator/src/lib/premadeProducts.ts](./generator/src/lib/premadeProducts.ts) lists the options
  in the premade product dropdown in [generator.tags.ioxio.dev](https://generator.tags.ioxio.dev),
  make sure the `product` field matches one of the filenames in
  [./demo_data/.well-known/product-passport/products/](./demo_data/.well-known/product-passport/products/).
- [./scanner/src/lib/dataproducts/\*.svelte](./scanner/src/lib/dataproducts/) has the components for
  rendering the data product in the [scanner.tags.ioxio.dev](https://scanner.tags.ioxio.dev)
  application.
- [./scanner/src/lib/dataproducts.ts](./scanner/src/lib/dataproducts.ts) maps the data product paths
  to the components to render them

So, if you were to e.g. add a new premade product of an existing type, you can just add it to
[premadeProducts.ts](./generator/src/lib/premadeProducts.ts).

If you wanted to add a new type of product, make sure you add the
[product metadata](./demo_data/.well-known/product-passport/products/) first, then update
[premadeProducts.ts](./generator/src/lib/premadeProducts.ts).

If you are adding supported data products or new sources for them to demo products, modify the
`supported_dataproducts` lists in
[product metadata](./demo_data/.well-known/product-passport/products/).

If you are adding new types of data products, create a
[component to render it](./scanner/src/lib/dataproducts/) and then add it to the
[map of supported data products](./scanner/src/lib/dataproducts.ts)

## Development

Prerequisites:

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Node 18+ LTS](https://nodejs.org/en/)
- [pnpm](https://pnpm.io/installation)

If you plan on contributing to the repository ensure you install
[pre-commit](https://pre-commit.com/#install) , and after checking out the repository ensure you run
`pre-commit install` in the repo root.

Both `generator` and `scanner` will actively use the API, so you will want that running when working
on either of the frontend components.

For testing you should first set up the `api`, then run `generator` and generate QR codes - we
suggest printing them at 5x5cm size for easier testing, then run the `scanner`. Using a USB web
camera will make testing the actual scanning easier.

### For Windows Users

To run `cairosvg` which is needed by the generator to generate the QR codes you might need to
install GTK+ for Windows.

- [GTK+ for Windows Runtime Environment Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

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

If you plan on testing new demo data locally, it is easiest by setting in `api/.env` an
`OVERRIDE_ISSUER_BASE_URL`. E.g. you can run `python -m http.server` in the `demo_data` folder to
host its contents locally, then in API's `.env` set:

```
OVERRIDE_ISSUER_BASE_URL=http://localhost:8000
```

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

To test data product rendering locally the easiest way is to generate an unsigned one off
[generator.tags.ioxio.dev](https://generator.tags.ioxio.dev) or a locally running version, then use
the `OVERRIDE_ISSUER_BASE_URL` setting for the [API](#api).

## Licensing

[BSD 3-clause](./LICENSE)

## Issues?

If you run into any issues, you can join our [IOXIO Community Slack](https://slack.ioxio.com/) and
discuss with us there, or [submit a new issue](https://github.com/ioxiocom/ioxio-tags/issues/new).
