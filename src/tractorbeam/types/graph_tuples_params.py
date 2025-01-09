# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GraphTuplesParams", "Tuple"]


class GraphTuplesParams(TypedDict, total=False):
    owner: Required[str]

    tuples: Required[Iterable[Tuple]]

    embeddings: Optional[Iterable[Iterable[float]]]


class Tuple(TypedDict, total=False):
    object: Required[str]
    """The object of the tuple"""

    predicate: Required[str]
    """The predicate of the tuple"""

    subject: Required[str]
    """The subject of the tuple"""
