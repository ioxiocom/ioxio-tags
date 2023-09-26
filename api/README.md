# Development tips

Run the tests while developing:

```shell
poetry run pytest-watch
```

If you want to also run the slow tests (QR code generation)

```shell
# Yes, the -- -- is really necessary
poetry run pytest-watch -- -- --runslow
```

# Generating keys

The API code depends on a `demo_key_private.pem` being in this folder. You can generate one, and an
accompanying public key, using these commands:

```shell
openssl genrsa -out demo_key_private.pem 2048
openssl rsa -in demo_key_private.pem -pubout -out demo_key_private.pub
```

Windows probably doesn't ship `openssl` by default, you might need to install it via e.g.
https://community.chocolatey.org/packages/openssl

Then if you want to test hosting the JWKS keys as well, you can run `poetry run python make_jwks.py`
to generate a `jwks.json` for hosting the public key.
