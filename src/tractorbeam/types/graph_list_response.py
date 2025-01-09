# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .graph import Graph
from .._models import BaseModel

__all__ = ["GraphListResponse"]


class GraphListResponse(BaseModel):
    graphs: List[Graph]
