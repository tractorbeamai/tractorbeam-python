# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TupleListParams"]


class TupleListParams(TypedDict, total=False):
    stream: bool
    """Whether to stream the tuples back as a stream of JSON server-sent events"""
