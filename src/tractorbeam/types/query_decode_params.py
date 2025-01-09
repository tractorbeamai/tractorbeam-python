# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["QueryDecodeParams"]


class QueryDecodeParams(TypedDict, total=False):
    depth: Required[int]

    graph_names: Required[List[str]]

    query: Required[str]
