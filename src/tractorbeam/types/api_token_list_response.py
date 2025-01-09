# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .api_token import APIToken

__all__ = ["APITokenListResponse"]


class APITokenListResponse(BaseModel):
    api_tokens: List[APIToken]
