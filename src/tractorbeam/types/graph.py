# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Graph"]


class Graph(BaseModel):
    created_at: str
    """The creation timestamp in ISO 8601 format"""

    name: str
    """The name of the graph, must match regex: ^[\\ww\\..-]{1,64}$"""

    owner: str
    """The owner of the graph, in the format "user*{id}" or "org*{id}" """

    tuple_count: Optional[int] = None
    """The number of tuples in the graph"""
