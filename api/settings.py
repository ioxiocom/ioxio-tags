from pathlib import Path
from typing import Literal, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


def _is_local_env(env: str) -> bool:
    return env in {"development", "unittest"}


class Settings(BaseSettings):
    #
    # Items to override for all deployments
    #

    ENV: str = "development"
    GCLOUD_PROJECT: str = "google-cloud-project"

    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    # Configuration for making valid signatures
    RSA_KID: str = "01"  # Key ID in JWKS
    RSA_ISS: str = "tags.ioxio.dev"  # Base domain
    RSA_PRIVATE_KEY: str = ""

    QR_CORRECTION_LEVEL: str = "Q"  # L = ~7%, M = ~15%, Q = ~25%, H = ~30%

    # RGB tuples
    QR_BACKGROUND: tuple[int, int, int] = (255, 255, 255)  # White
    QR_FOREGROUND: tuple[int, int, int] = (0, 0, 0)  # Black

    # Set to e.g. http://localhost:8000 for local testing
    OVERRIDE_ISSUER_BASE_URL: Optional[str] = None

    #
    # For local only
    #

    def is_local_env(self):
        return _is_local_env(self.ENV)

    model_config = SettingsConfigDict(env_file=".env")


conf = Settings()
if conf.is_local_env():
    conf.LOG_LEVEL = "DEBUG"
    conf.RSA_PRIVATE_KEY = (Path(__file__).parent / "demo_key_private.pem").read_text(encoding="utf-8")
