# import warnings
# warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")  # fake_useragent
from unittest.mock import patch

from httpx import AsyncClient

import pytest
from main import app
from settings import conf
from testdata import TEST_QR_IMG, TEST_FAKE_HOSTED_FILES

pytest_plugins = ('pytest_asyncio',)


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture
def prepare_settings():
    print("In unittest env")
    conf.ENV = "unittest"


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://localhost:8081") as c:
        yield c


@pytest.fixture
async def fake_make_image():
    def _make_image(payload: bytes, frame_type: str) -> bytes:
        return TEST_QR_IMG

    with patch('app.tag.make_image', _make_image):
        yield


@pytest.fixture
async def fake_hosting():
    async def _fetch_json_file(url) -> bytes:
        if url in TEST_FAKE_HOSTED_FILES:
            return TEST_FAKE_HOSTED_FILES[url]

        raise NotImplementedError(f"Unexpected request to fetch {url}, which we have no test data for")

    with patch('app.tag.fetch_json_file', _fetch_json_file):
        yield
