#
# TODO MOVE TO A rsa-to-jwks PyPI package
#

import json
from pathlib import Path

import sys
import typer
from jose import jwk, constants

# Add .. to path to load settings.py
sys.path.append(str(Path(__file__).parent.parent))
import settings

app = typer.Typer()


@app.command()
def main():
    print(f"Generating JWKS file for public key")

    key = jwk.RSAKey(algorithm=constants.ALGORITHMS.RS256, key=settings.RSA_PUBLIC_KEY)

    raw_data = {"keys": [key.to_dict()]}
    print(raw_data)

    json_data = json.dumps(raw_data, indent=2)

    filename = Path(__file__).parent / "jwks.json"
    Path(filename).write_text(json_data, encoding="utf-8")

    print(f"Generated {filename}, place it in `.well-known/jwks.json` and point to it from your metadata.")


if __name__ == "__main__":
    typer.run(main)
