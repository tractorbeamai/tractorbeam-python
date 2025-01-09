# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["GraphQueryResponse"]


class GraphQueryResponse(BaseModel):
    bindings: List[Dict[str, str]]
