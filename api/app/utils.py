import anyio
import httpx
from httpx import RequestError
import validators


async def fetch_json_file(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
        except anyio.EndOfStream:
            raise RequestError(f"Failed to connect to {url}")

        res.raise_for_status()

        return res.json()


def domain_validator(domain: str) -> str:
    assert validators.domain(domain), f"{domain} is not a valid domain name"
    return domain
