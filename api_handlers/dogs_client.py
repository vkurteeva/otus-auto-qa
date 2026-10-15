from typing import Optional
from api_handlers.http_client import HTTPClient
from models.dogs import GetListResponse, ImagesResponse


class ApiDogsTest(HTTPClient):
    def __init__(self) -> None:
        super().__init__("https://dog.ceo/api")

    def get_list_all(self) -> GetListResponse:
        return self.get("/breeds/list/all", response_model=GetListResponse)

    def get_list_by_breed(self, breed: str) -> GetListResponse:
        return self.get(f"/breed/{breed}/list/all", response_model=GetListResponse)

    def get_random_image(self, count: Optional[int] = None) -> ImagesResponse:
        path = "/breeds/image/random"
        if count is not None:
            path = f"{path}/{count}"
        return self.get(path, response_model=ImagesResponse)

    def get_image_by_breed(self, breed: str) -> ImagesResponse:
        return self.get(f"/breed/{breed}/images", response_model=ImagesResponse)

    def get_random_image_by_breed(
        self, breed: str, count: Optional[int] = None
    ) -> ImagesResponse:
        path = f"/breed/{breed}/images/random"
        if count is not None:
            path = f"{path}/{count}"
        return self.get(path, response_model=ImagesResponse)
