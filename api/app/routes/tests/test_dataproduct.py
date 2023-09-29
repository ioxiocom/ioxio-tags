from httpx import AsyncClient


# Test verifying
async def test_tag_verify_v1_ok(client: AsyncClient, fake_dataspace):
    payload = {
        "product": "nice-battery",
        "id": "abc-123"
    }

    r = await client.post(
        "/dataproduct/fetch/DigitalProductPassport/Energy/Battery/BatteryProduct?source=janne",
        json=payload
    )

    from pprint import pprint
    pprint(r.json())
    assert r.status_code == 200
    result = r.json()
    assert result["some"] == "response"
