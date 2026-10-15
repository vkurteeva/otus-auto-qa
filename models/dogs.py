from pydantic import BaseModel, HttpUrl
from typing import Dict, List, Union


class GetListResponse(BaseModel):
    message: Dict[str, List[str]]
    status: str


class ImagesResponse(BaseModel):
    message: Union[HttpUrl, List[HttpUrl]]
    status: str
