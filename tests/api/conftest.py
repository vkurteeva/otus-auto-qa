import requests
import pytest
from api_handlers.dogs_client import ApiDogsTest as Api
from api_handlers.obdb_client import ObdbClient as Api
from api_handlers.jsonplaceholder_client import JsonplaceholderClient as Api


@pytest.fixture
def api_client():
    return Api()
