import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="Target URL to check"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        type=int,
        help="Expected HTTP status code"
    )


@pytest.fixture
def target_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")


def test_url_status_code(target_url, expected_status):
    response = requests.get(target_url)
    assert response.status_code == expected_status
