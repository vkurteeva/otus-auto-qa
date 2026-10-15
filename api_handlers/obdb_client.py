from typing import Optional

from api_handlers.http_client import HTTPClient
from models.obdb import GetListResponse


class ObdbClient(HTTPClient):
    def __init__(self):
        base_url = "https://api.openbrewerydb.org/v1"
        super().__init__(base_url)

    def get_list(
        self,
        by_city: Optional[str] = None,
        by_country: Optional[str] = None,
        by_dist: Optional[str] = None,
        by_name: Optional[str] = None,
        by_state: Optional[str] = None,
        by_postal: Optional[str] = None,
        by_type: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> GetListResponse:
        filtered_params = {
            "by_city": by_city,
            "by_country": by_country,
            "by_dist": by_dist,
            "by_name": by_name,
            "by_state": by_state,
            "by_postal": by_postal,
            "by_type": by_type,
            "page": page,
            "per_page": per_page,
            "sort": sort,
        }

        return self.get(
            path="/breweries", params=filtered_params, response_model=GetListResponse
        )
