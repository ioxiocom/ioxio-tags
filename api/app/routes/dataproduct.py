from typing import Any, Annotated

from fastapi import APIRouter, Body, Path
from fastapi.responses import JSONResponse
from pydantic import AfterValidator

import app.dataproduct as dataproduct
from app.errors import TagsError
from app.responses import TagsErrorResponse
from app.utils import domain_validator

router = APIRouter(prefix="/dataproduct")


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

        if product_path == "DigitalProductPassport/Textile/Garment/MaintenanceLog_v0.1":
            import app.routes.mocks.test_garment_maintenance_log_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )
        elif product_path == "DigitalProductPassport/Textile/Garment/BillofMaterials_v0.1":
            import app.routes.mocks.test_garment_bill_of_materials_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )
        elif product_path == "DigitalProductPassport/Product/CarbonFootprint_v0.1":
            import app.routes.mocks.test_product_carbon_footprint_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )
        elif product_path == "DigitalProductPassport/Textile/Garment/MaterialDisclosureSheet_v0.1":
            import app.routes.mocks.test_garment_material_disclosure_sheet_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )
        elif product_path == "DigitalProductPassport/Textile/Garment/ManufacturerInformation_v0.1":
            import app.routes.mocks.test_garment_manufacturer_information_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )
        elif product_path == "DigitalProductPassport/Textile/Garment/ProductDataSheet_v0.1":
            import app.routes.mocks.test_garment_product_data_sheet_v0_1 as m

            return JSONResponse(
                status_code=200,
                content=m.resp,
            )

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
