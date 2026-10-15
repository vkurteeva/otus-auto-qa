from typing import Optional, Type, Any, TypeVar
import requests
from pydantic import BaseModel, ValidationError, TypeAdapter

ModelT = TypeVar("ModelT")


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _send_request(
        self,
        method: str,
        path: str,
        response_model: Optional[Type[ModelT]] = None,
        json_data: Optional[Any] = None,
        **kwargs: Any,
    ) -> Any:
        clean_path = f"/{path.lstrip('/')}"
        url = f"{self.base_url}{clean_path}"

        headers = kwargs.pop("headers", {})
        if json_data is not None:
            headers["Content-Type"] = "application/json"

        kwargs.pop("response_model", None)

        response = requests.request(
            method=method, url=url, headers=headers, json=json_data, **kwargs
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            try:
                server_error = response.json()
                error_msg = server_error.get("message", str(e))
            except (requests.exceptions.JSONDecodeError, ValueError):
                error_msg = response.text
            raise AssertionError(
                f"API Error [{response.status_code}] на URL {url}. Ответ сервера: {error_msg}"
            ) from e

        if response_model:
            try:
                return TypeAdapter(response_model).validate_python(response.json())
            except ValidationError as e:
                model_name = getattr(response_model, "__name__", str(response_model))
                raise AssertionError(
                    f"Ошибка валидации Pydantic для модели {model_name} на URL {url}. "
                    f"Ответ сервера: {response.json()}"
                ) from e
        return response.json()

    def get(
        self, path: str, response_model: Optional[Type[ModelT]] = None, **kwargs: Any
    ) -> Any:
        return self._send_request(
            method="GET", path=path, response_model=response_model, **kwargs
        )

    def post(
        self,
        path: str,
        data: Optional[Any] = None,
        response_model: Optional[Type[ModelT]] = None,
        **kwargs: Any,
    ) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump(mode="json")
        return self._send_request(
            method="POST",
            path=path,
            response_model=response_model,
            json_data=data,
            **kwargs,
        )

    def put(
        self,
        path: str,
        data: Optional[Any] = None,
        response_model: Optional[Type[ModelT]] = None,
        **kwargs: Any,
    ) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump(mode="json")
        return self._send_request(
            method="PUT",
            path=path,
            response_model=response_model,
            json_data=data,
            **kwargs,
        )

    def patch(
        self,
        path: str,
        data: Optional[Any] = None,
        response_model: Optional[Type[ModelT]] = None,
        **kwargs: Any,
    ) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump(mode="json")
        return self._send_request(
            method="PATCH",
            path=path,
            response_model=response_model,
            json_data=data,
            **kwargs,
        )

    def delete(
        self, path: str, response_model: Optional[Type[ModelT]] = None, **kwargs: Any
    ) -> Any:
        return self._send_request(
            method="DELETE", path=path, response_model=response_model, **kwargs
        )
