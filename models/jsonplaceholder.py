from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None
    userId: Optional[int] = None


class PostCreateRequest(BaseModel):
    id: Optional[int] = None
    title: str
    body: str
    userId: int


class PostUpdateRequest(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None
    userId: Optional[int] = None
