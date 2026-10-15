from typing import Union, Dict, Any, Optional, List
from api_handlers.http_client import HTTPClient
from models.jsonplaceholder import PostCreateRequest, PostUpdateRequest, Response


class JsonplaceholderClient(HTTPClient):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")

    def get_post_by_id(self, post_id: int) -> Response:
        return self.get(path=f"/posts/{post_id}", response_model=Response)

    def get_posts(self, user_id: Optional[int] = None) -> List[Response]:
        params = {"userId": user_id} if user_id is not None else None
        return self.get(path="/posts", params=params, response_model=List[Response])

    def create_post(
        self, post_data: Union[PostCreateRequest, Dict[str, Any]]
    ) -> Response:
        return self.post(path="/posts", data=post_data, response_model=Response)

    def update_post_put(
        self, post_id: int, post_data: Union[PostCreateRequest, Dict[str, Any]]
    ) -> Response:
        return self.put(
            path=f"/posts/{post_id}", data=post_data, response_model=Response
        )

    def update_post_patch(
        self, post_id: int, post_data: Union[PostUpdateRequest, Dict[str, Any]]
    ) -> Response:
        return self.patch(
            path=f"/posts/{post_id}", data=post_data, response_model=Response
        )

    def delete_post(self, post_id: int) -> Dict[str, Any]:
        return self.delete(path=f"/posts/{post_id}")
