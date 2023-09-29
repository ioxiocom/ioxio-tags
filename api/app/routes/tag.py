from typing import Annotated

from fastapi import APIRouter, Response
from pydantic import BaseModel, Field, AfterValidator
from starlette import status
from starlette.responses import JSONResponse

from app.errors import CannotSignInvalidIssuer, TagsError
from app.responses import TagsErrorResponse
from app.tag import make_cose_code, make_url_code, verify_code, fetch_metadata
from app.utils import domain_validator
from settings import conf

router = APIRouter(prefix="/tag")


def filename_header(filename: str) -> dict:
    return {
        f"Content-Disposition": f"attachment; filename={filename}"
    }


class VerifyV1Request(BaseModel):
    code: str = Field(..., title="Scanned text from QR Code")


class MetadataV1Request(BaseModel):
    iss: Annotated[str, AfterValidator(domain_validator)] = Field(...,
                                                                  title="Issuer of the code, aka iss from the QR code data")
    product: str = Field(..., title="Product category, aka product from the QR code data")


class SupportedDataproduct(BaseModel):
    path: str = Field(..., title="Path for the data product on the dataspace",
                      examples=["DPP/Energy/Battery/ProductDataSheet_v0.1"])
    source: str = Field(..., title="The supported source for this data product on the dataspace")


class MetadataV1Response(BaseModel):
    logo_url: str = Field(..., title="URL to the logo of the issuer")
    image_url: str = Field(..., title="URL to a product picture")
    product_dataspace: str = Field(..., title="Base domain of the dataspace the product data will be on")
    names: dict[str, str] = Field(...,
                                  title="Map of locale in IETF BCP 47 format (en-US) to the name of the product in that language")
    supported_dataproducts: list[SupportedDataproduct] = Field(...,
                                                               title="List of supported data products for this product")


class GenerateSecureV1Request(BaseModel):
    iss: Annotated[str, AfterValidator(domain_validator)] = Field(..., title="Issuer to be put in the code")
    product: str = Field(..., title="Product category to be put in the code")
    id: str = Field(..., title="Unique ID to be put in the code")
    valid: bool = Field(..., title="If the generated signature should be valid or not")


class GenerateURLV1Request(BaseModel):
    iss: Annotated[str, AfterValidator(domain_validator)] = Field(..., title="Issuer to be put in the code")
    product: str = Field(..., title="Product category to be put in the code")
    id: str = Field(..., title="Unique ID to be put in the code")


@router.post("/verify/v1/",
             summary="Verify the COSE signature in a IOXIO Tag -code",
             status_code=status.HTTP_204_NO_CONTENT,
             responses={400: {"model": TagsErrorResponse}},
             tags=["tag"],
             )
async def verify_v1(data: VerifyV1Request):
    try:
        await verify_code(data.code)
    except TagsError as e:
        return JSONResponse(
            status_code=400,
            content=TagsErrorResponse(error=e.error, code=e.code).model_dump()
        )


@router.post("/metadata/v1/",
             summary="Fetch and parse the metadata necessary for the tag from the issuer's published metadata",
             response_model=MetadataV1Response,
             responses={400: {"model": TagsErrorResponse}},
             tags=["tag"],
             )
async def metadata_v1(data: MetadataV1Request):
    try:
        return await fetch_metadata(data.iss, data.product)
    except TagsError as e:
        return JSONResponse(
            status_code=400,
            content=TagsErrorResponse(error=e.error, code=e.code).model_dump()
        )


@router.post("/generate/secure/v1/",
             summary="Generate a new IOXIO Tag with COSE signature",
             response_class=Response,
             responses={
                 200: {"content": {"image/png": {}}},
                 400: {"model": TagsErrorResponse}
             },
             tags=["tag"],
             )
async def generate_secure_v1(data: GenerateSecureV1Request):
    try:
        filename, image_content = make_cose_code(
            iss=data.iss,
            product=data.product,
            id=data.id,
            valid=data.valid
        )
    except CannotSignInvalidIssuer:
        return JSONResponse(
            status_code=400,
            content=TagsErrorResponse(
                error=f"Cannot sign, the issuer does not match available private key. Expected {conf.RSA_ISS}, got {data.iss}",
                code="cannot_sign_issuer_mismatch"
            ).model_dump()
        )

    return Response(
        content=image_content,
        headers=filename_header(filename),
        media_type="image/png",
    )


@router.post("/generate/url/v1/",
             summary="Generate a new simple IOXIO Tag with only URL data",
             response_class=Response,
             responses={
                 200: {"content": {"image/png": {}}},
                 400: {"model": TagsErrorResponse}
             },
             tags=["tag"],
             )
async def generate_url_v1(data: GenerateURLV1Request):
    filename, image_content = make_url_code(
        iss=data.iss,
        product=data.product,
        id=data.id,
    )

    return Response(
        content=image_content,
        headers=filename_header(filename),
        media_type="image/png",
    )
