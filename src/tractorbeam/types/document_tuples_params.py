# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DocumentTuplesParams"]


class DocumentTuplesParams(TypedDict, total=False):
    stream: bool
    """Whether to stream the tuples back as a stream of JSON server-sent events"""

    target_graph_name: Optional[str]
    """The name of the target graph to add tuples to"""

    target_graph_owner: Optional[str]
    """The owner of the target graph to add tuples to"""
