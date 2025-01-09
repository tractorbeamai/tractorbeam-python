# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.graphs import tuple_create_params
from ...types.graphs.tuple_create_response import TupleCreateResponse

__all__ = ["TuplesResource", "AsyncTuplesResource"]


class TuplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TuplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return TuplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tractorbeam-python#with_streaming_response
        """
        return TuplesResourceWithStreamingResponse(self)

    def create(
        self,
        name: str,
        *,
        owner: str,
        tuples: Iterable[tuple_create_params.Tuple],
        embeddings: Optional[Iterable[Iterable[float]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TupleCreateResponse:
        """
        Insert tuples into an existing graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            f"/graphs/{owner}/{name}/tuples",
            body=maybe_transform(
                {
                    "tuples": tuples,
                    "embeddings": embeddings,
                },
                tuple_create_params.TupleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TupleCreateResponse,
        )


class AsyncTuplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTuplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTuplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tractorbeam-python#with_streaming_response
        """
        return AsyncTuplesResourceWithStreamingResponse(self)

    async def create(
        self,
        name: str,
        *,
        owner: str,
        tuples: Iterable[tuple_create_params.Tuple],
        embeddings: Optional[Iterable[Iterable[float]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TupleCreateResponse:
        """
        Insert tuples into an existing graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            f"/graphs/{owner}/{name}/tuples",
            body=await async_maybe_transform(
                {
                    "tuples": tuples,
                    "embeddings": embeddings,
                },
                tuple_create_params.TupleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TupleCreateResponse,
        )


class TuplesResourceWithRawResponse:
    def __init__(self, tuples: TuplesResource) -> None:
        self._tuples = tuples

        self.create = to_raw_response_wrapper(
            tuples.create,
        )


class AsyncTuplesResourceWithRawResponse:
    def __init__(self, tuples: AsyncTuplesResource) -> None:
        self._tuples = tuples

        self.create = async_to_raw_response_wrapper(
            tuples.create,
        )


class TuplesResourceWithStreamingResponse:
    def __init__(self, tuples: TuplesResource) -> None:
        self._tuples = tuples

        self.create = to_streamed_response_wrapper(
            tuples.create,
        )


class AsyncTuplesResourceWithStreamingResponse:
    def __init__(self, tuples: AsyncTuplesResource) -> None:
        self._tuples = tuples

        self.create = async_to_streamed_response_wrapper(
            tuples.create,
        )
