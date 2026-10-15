from enum import Enum
from pydantic import BaseModel, RootModel
from typing import Optional


class BreweryType(str, Enum):
    MICRO = "micro"
    NANO = "nano"
    REGIONAL = "regional"
    BREWPUB = "brewpub"
    LARGE = "large"
    PLANNING = "planning"
    BAR = "bar"
    CONTRACT = "contract"
    PROPRIETOR = "proprietor"
    CLOSED = "closed"
    TAPROOM = "taproom"
    BEERGARDEN = "beergarden"


class BreweryModel(BaseModel):
    id: str
    name: str
    brewery_type: Optional[BreweryType] = None
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None


class GetListResponse(RootModel[list[BreweryModel]]):
    pass
