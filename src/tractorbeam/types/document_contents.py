# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["DocumentContents"]


class DocumentContents(BaseModel):
    contents: List[int]
    """The binary contents of the document"""
