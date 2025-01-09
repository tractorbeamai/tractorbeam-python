# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the document"""

    file: Optional[Iterable[int]]
    """The file content of the document"""

    text: Optional[str]
    """The text content of the document"""
