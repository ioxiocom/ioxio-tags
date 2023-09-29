import anyio
import httpx
from httpx import RequestError


async def fetch_json_file(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url)
        except anyio.EndOfStream:
            raise RequestError(f"Failed to connect to {url}")

        res.raise_for_status()

        return res.json()
