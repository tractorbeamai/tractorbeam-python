# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["GraphGetTuplesResponse", "Tuple"]


class Tuple(BaseModel):
    object: str
    """The object of the tuple"""

    predicate: str
    """The predicate of the tuple"""

    subject: str
    """The subject of the tuple"""


class GraphGetTuplesResponse(BaseModel):
    tuples: List[Tuple]
