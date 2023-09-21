from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/dataproduct")


class DataProductFetchRequest(BaseModel):
    pass


class DataProductFetchResponse(BaseModel):
    pass


@router.post("/fetch/{dataspace_domain}/{product_path:path}",
            summary="Fetch a data product from the dataspace",
            response_model=DataProductFetchRequest,
            tags=["dataproduct"],
            )
async def account_status(dataspace_domain: str, product_path: str):
    pass
