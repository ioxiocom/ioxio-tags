"""
Wrapper for running pnpm run import-api for pre-commit
"""
import os
from hashlib import sha256
from pathlib import Path

HASH_FILE = Path("openapi_hash.sha256")
OPENAPI_FILE = Path("openapi.json")


def run_import_api(cwd: str):
    os.chdir(cwd)
    os.system("pnpm run import-api")  # nosec
    os.chdir("..")


def import_api():
    old_hash = ""
    if HASH_FILE.exists():
        old_hash = HASH_FILE.read_text(encoding="utf-8")

    new_hash = sha256(OPENAPI_FILE.read_bytes()).hexdigest()

    if old_hash != new_hash:
        print("Need to update openapi.ts files")
        run_import_api("generator")
        run_import_api("scanner")
        HASH_FILE.write_text(new_hash, encoding="utf-8")
    else:
        print("openapi.ts files are up-to-date")


if __name__ == "__main__":
    import_api()
