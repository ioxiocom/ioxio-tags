import logging
import random
import string
import sys
import traceback
from os import environ

import orjson
from loguru import logger

from settings import conf

# Fix import autocomplete
logger = logger

LOG_LEVEL = conf.LOG_LEVEL
DEFAULT_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    # Uncomment for detailed logs for hard debugging sessions
    # "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level> "
    "{extra}"
)


def gcloud_serializer(message):
    """
    Serializer for tweaking log record so it can be parsed by Google Cloud
    """
    # https://github.com/Delgan/loguru/issues/203
    record = message.record

    if message.record["exception"] is None:
        severity = record["level"].name
        raw_msg = record["message"]
        message = record["message"] + " | " + str(record["extra"])
    else:
        severity = "CRITICAL"
        exc = message.record["exception"]
        tb = traceback.format_exception(exc.type, exc.value, exc.traceback)
        raw_msg = "".join(tb)
        message = record["message"] + raw_msg

    google_trace_id = record["extra"].pop("google_trace_id", None)

    log_data = {
        "severity": severity,
        "raw": raw_msg,  # Displayed while expanding log record
        "message": message,  # Displayed directly in log viewer
        "extra": record["extra"],
        "time": record["time"],
    }
    if google_trace_id:
        log_data[
            "logging.googleapis.com/trace"
        ] = f"projects/{conf.GCLOUD_PROJECT}/traces/{google_trace_id}"

    serialized = orjson.dumps(log_data, default=str).decode("utf-8")
    print(serialized, file=sys.stderr)


async def inject_request_id_middleware(request, call_next):
    """
    FastAPI middleware for injecting request_id and Google Trace ID if exists.
    Usage: `app.middleware("http")(inject_request_id_middleware)`
    """
    request_id = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=6))  # nosec, this is not used for security
    context = {"request_id": request_id}
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    if trace_header:
        context["google_trace_id"] = trace_header.split("/")[0]
    with logger.contextualize(**context):
        return await call_next(request)


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        logger_opt = logger.opt(depth=7, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def init_logging(logger_, local_env: bool):
    """
    Set up logging handlers. Output format is applied based on running environment

    :param logger_: Logger instance
    :param local_env: Whether current environment is local
    """

    # https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]

    # remove every other logger's handlers and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        # Skip over unwanted access logging
        if name == "uvicorn.access":
            continue

        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger_.remove()
    if local_env:
        logger_.add(
            sys.stdout,
            format=environ.get("LOGURU_FORMAT", DEFAULT_FORMAT),
            colorize=True,
            level=LOG_LEVEL,
        )
    else:
        logger_.add(gcloud_serializer, level=LOG_LEVEL)


init_logging(logger, conf.is_local_env())
