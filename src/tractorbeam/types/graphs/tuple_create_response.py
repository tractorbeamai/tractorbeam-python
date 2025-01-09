# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["TupleCreateResponse"]


class TupleCreateResponse(BaseModel):
    inserted: int
    """The number of tuples inserted"""
