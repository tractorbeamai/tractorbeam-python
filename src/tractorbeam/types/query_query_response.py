# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["QueryQueryResponse"]


class QueryQueryResponse(BaseModel):
    chains: List[str]
