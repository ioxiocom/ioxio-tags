from urllib.parse import quote_plus

import anyio
import httpx
from async_lru import alru_cache

from app.errors import TagsError
from app.utils import fetch_json_file


@alru_cache(maxsize=4)
async def get_dataspace_configuration(dataspace: str) -> dict:
    return await fetch_json_file(f"https://{dataspace}/.well-known/dataspace/dataspace-configuration.json")


async def fetch_dataproduct(dataspace: str, product: str, source: str, payload: dict) -> httpx.Response:
    url = dataspace
    try:
        config = await get_dataspace_configuration(dataspace)
        gateway = config["product_gateway_url"]
        url = f"{gateway}/{product}?source={quote_plus(source)}"

        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=payload)
            return res
    except anyio.EndOfStream:
        raise TagsError(
            error=f"Failed to connect to {url}",
            code="invalid_url_cannot_connect",
        )
    except httpx.ConnectError:
        raise TagsError(
            error=f"Failed to connect to {url}",
            code="invalid_url_cannot_connect",
        )
