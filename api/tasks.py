import json
import socket
from os import environ, system
from pathlib import Path

import typer
import uvicorn
from deepdiff import DeepDiff
from uvicorn.supervisors import ChangeReload

OPENAPI_SPEC_FILE = "../openapi.json"
DEV_ENV = {"PORT": environ.get("PORT", "8081")}
app = typer.Typer()


def get_listen_host(force_ipv6: bool = False) -> str:
    host = "0.0.0.0"  # nosec, not a mistake

    # Try to figure out if we're running in IPv6 land
    if force_ipv6 or socket.gethostbyname("localhost") != "127.0.0.1":
        host = "::"  # nosec, still not a mistake

    return host


def uvicorn_common(force_ipv6: bool = False):
    return {
        "app": "main:app",
        "host": get_listen_host(force_ipv6),
        "port": int(environ.get("PORT", "8080")),
        "headers": [("server", "IOXIO Tags API")],
        "access_log": False,
    }


@app.command()
def dev(ipv6: bool = False):
    system("poetry install")  # nosec

    environ.update(DEV_ENV)

    reload_dirs = [str(Path(__file__).parent.absolute())]
    config = uvicorn.Config(
        log_level="debug",
        reload=True,
        reload_dirs=reload_dirs,
        **uvicorn_common(ipv6),
    )
    server = uvicorn.Server(config)

    from app.log import \
        logger  # noqa, must be imported before running supervisor
    _ = logger

    supervisor = ChangeReload(config, target=server.run, sockets=[config.bind_socket()])
    supervisor.run()


@app.command()
def serve():
    server = uvicorn.Server(
        uvicorn.Config(
            forwarded_allow_ips="*",
            proxy_headers=True,
            reload=False,
            **uvicorn_common(),
        ),
    )
    server.run()


@app.command()
def export_api():
    from main import app

    openapi_file = Path(OPENAPI_SPEC_FILE)
    openapi_spec = app.openapi()
    spec_json = json.dumps(openapi_spec, indent=2)

    content = spec_json.replace("\r\n", "\n").encode("utf-8")

    try:
        old_openapi_spec = json.loads(openapi_file.read_bytes())
    except FileNotFoundError:
        old_openapi_spec = {}

    if DeepDiff(openapi_spec, old_openapi_spec, ignore_order=True) != {}:
        openapi_file.write_bytes(content)
        print(f"OpenAPI spec written to {OPENAPI_SPEC_FILE}")
    else:
        print("OpenAPI spec does not require updates")


def run_command():
    # Fuck Typer is incredibly stupid
    import sys

    first = sys.argv[0]
    if "/" in first:
        first = first.split("/")[-1]

    if "\\" in first:
        first = first.split("\\")[-1]

    if first.endswith(".cmd"):
        first = first[:-4]

    args = [
        sys.argv[0],
        first
    ]

    if len(sys.argv) > 1:
        args += sys.argv[1:]

    sys.argv = args
    app()


if __name__ == "__main__":
    app()
