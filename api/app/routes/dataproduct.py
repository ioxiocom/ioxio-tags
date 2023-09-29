from typing import Any, Annotated

from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from pydantic import AfterValidator

import app.dataproduct as dataproduct
from app.errors import TagsError
from app.responses import TagsErrorResponse
from app.utils import domain_validator

router = APIRouter(prefix="/dataproduct")


from fastapi import Path


@router.post("/fetch/{dataspace_domain}/{product_path:path}",
             summary="Fetch a data product from the dataspace. Documentation for each is in Dataspace's definitions.",
             tags=["dataproduct"],
             )
async def dataproduct_fetch(
        product_path: str,
        source: str,
        dataspace_domain: str = Path(annotation=Annotated[str, AfterValidator(domain_validator)]),
        payload: Any = Body(),
):
    try:
        def _filter_headers(headers: dict) -> dict:
            valid_headers = [
                "content-type",
                "x-powered-by",
            ]

            return {
                h: v
                for h, v in headers.items()
                if h.lower() in valid_headers
            }

        result = await dataproduct.fetch_dataproduct(dataspace_domain, product_path, source, payload)
        return JSONResponse(
            status_code=result.status_code,
            headers=_filter_headers(result.headers),
            content=result.json(),
        )
    except TagsError as e:
        return JSONResponse(
            status_code=500,
            content=TagsErrorResponse(error=e.error, code=e.code).model_dump()
        )
