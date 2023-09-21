"""
Wrapper for running poetry run export-api in the "api" directory for pre-commit
"""
import os


def export_api():
    os.chdir("api")
    os.system("poetry run export-api")  # nosec


if __name__ == "__main__":
    export_api()
