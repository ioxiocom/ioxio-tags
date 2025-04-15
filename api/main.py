from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_standalone_docs import StandaloneDocs

from app.log import inject_request_id_middleware, logger
from app.routes.dataproduct import router as dataproduct_router
from app.routes.tag import router as tag_router
from settings import conf

APP_KWARGS = {}
if not conf.is_local_env():
    APP_KWARGS["debug"] = False
    origins = [
        "https://tags.ioxio.io",
        "https://generator.tags.ioxio.io",
        "https://scanner.tags.ioxio.io",
        "https://tags.ioxio.dev",
        "https://generator.tags.ioxio.dev",
        "https://scanner.tags.ioxio.dev",
    ]
else:
    APP_KWARGS["debug"] = True
    origins = [
        "http://localhost",
        "http://localhost:5173",
        # Port 5174 added because running both scanner and generator locally
        # makes one of them use the next available port. This can be removed
        # once a default port is set for both.
        "http://localhost:5174",
        "http://localhost:4173",
    ]


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting api for {conf.ENV} environment")
    yield


app = FastAPI(
    title="IOXIO Tags API",
    version="1.0.0",
    lifespan=lifespan,
    **APP_KWARGS,
)

StandaloneDocs(app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.middleware("http")(inject_request_id_middleware)
app.include_router(dataproduct_router)
app.include_router(tag_router)


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "0"  # Content-Security-Policy is safer
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"  # 1 year
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers[
        "Permissions-Policy"] = "camera=(), microphone=(), display-capture=(), geolocation=(), payment=(), autoplay=()"
    response.headers["Content-Security-Policy"] = "; ".join([
        "default-src 'self'",
        "img-src data: 'self'",
        "script-src 'self' 'unsafe-inline'",
        "style-src 'self' 'unsafe-inline'",
        "worker-src blob:"
    ])
    return response
