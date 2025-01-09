# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["GraphTuplesResponse"]


class GraphTuplesResponse(BaseModel):
    inserted: int
    """The number of tuples inserted"""
