import pytest
from httpx import AsyncClient
from starlette import status

from app.responses import TagsErrorResponse
from app.routes.tag import GenerateURLV1Request, GenerateSecureV1Request, VerifyV1Request
from settings import conf
from testdata import TEST_CODE


# Test verifying
async def test_tag_verify_v1_ok(client: AsyncClient, fake_hosting):
    verify_params = VerifyV1Request(code=TEST_CODE)
    r = await client.post("/tag/verify/v1/", json=verify_params.model_dump())
    if r.status_code != status.HTTP_204_NO_CONTENT:
        response = r.json()
        print(response)
    assert r.status_code == status.HTTP_204_NO_CONTENT


# Test that verification can also fail
async def test_tag_verify_v1_invalid(client: AsyncClient, fake_hosting):
    verify_params = VerifyV1Request(code=TEST_CODE + "1")
    r = await client.post("/tag/verify/v1/", json=verify_params.model_dump())
    response = r.json()
    print(response)
    assert r.status_code == status.HTTP_400_BAD_REQUEST

    resp = TagsErrorResponse(**r.json())
    assert "failed Base45 decode" in resp.error
    assert resp.code == "signature_verification_failed"


# Test generating simple URL tags (only validations etc.)
async def test_fake_tag_generate_url_v1(client: AsyncClient, fake_make_image):
    generate_params = GenerateURLV1Request(
        iss="arbitrary.example.com",
        product="amazing-product",
        id="abc123-serial-xyz",
    )

    r = await client.post("/tag/generate/url/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024


# Ensure we can't sign for arbitrary domains
async def test_fake_tag_generate_secure_v1_invalid_iss(client: AsyncClient, fake_make_image):
    generate_params = GenerateSecureV1Request(
        iss="another." + conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=True
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert not r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "application/json"

    resp = TagsErrorResponse(**r.json())
    assert resp.code == "cannot_sign_issuer_mismatch"


# Ensure we can generate invalid signatures for arbitrary domains
async def test_fake_tag_generate_secure_v1_unsigned_arbitrary(client: AsyncClient, fake_make_image):
    generate_params = GenerateSecureV1Request(
        iss="another." + conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=False
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024


# Ensure we can sign for configured domain
async def test_fake_tag_generate_secure_v1_valid(client: AsyncClient, fake_make_image):
    generate_params = GenerateSecureV1Request(
        iss=conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=True
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024


#
# Slow actual image generation tests
#

# Test generating simple URL tags
@pytest.mark.slow
async def test_tag_generate_url_v1(client: AsyncClient):
    generate_params = GenerateURLV1Request(
        iss="arbitrary.example.com",
        product="amazing-product",
        id="abc123-serial-xyz",
    )

    r = await client.post("/tag/generate/url/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024


# Ensure we can't sign for arbitrary domains
@pytest.mark.slow
async def test_tag_generate_secure_v1_invalid_iss(client: AsyncClient):
    generate_params = GenerateSecureV1Request(
        iss="another." + conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=True
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert not r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "application/json"

    resp = TagsErrorResponse(**r.json())
    assert resp.code == "cannot_sign_issuer_mismatch"


# Ensure we can generate invalid signatures for arbitrary domains
@pytest.mark.slow
async def test_tag_generate_secure_v1_unsigned_arbitrary(client: AsyncClient):
    generate_params = GenerateSecureV1Request(
        iss="another." + conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=False
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024


# Ensure we can sign for configured domain
@pytest.mark.slow
async def test_tag_generate_secure_v1_valid(client: AsyncClient):
    generate_params = GenerateSecureV1Request(
        iss=conf.RSA_ISS,
        product="amazing-product",
        id="abc123-serial-xyz",
        valid=True
    )

    r = await client.post("/tag/generate/secure/v1/", json=generate_params.model_dump())
    assert r.status_code == status.HTTP_200_OK
    assert r.headers.get("content-disposition", "").startswith("attachment; ")
    assert r.headers.get("content-type", "") == "image/png"

    # >= 1kB probably means an actual image was sent
    body = r.read()
    assert len(body) > 1024
