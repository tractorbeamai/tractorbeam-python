# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.documents import tuple_list_params

__all__ = ["TuplesResource", "AsyncTuplesResource"]


class TuplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TuplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return TuplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#with_streaming_response
        """
        return TuplesResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Extract tuples from a document by its ID.

        If streaming is enabled, the response
        will be a stream of tuples as JSON server-sent events. This endpoint requires
        calling our external inference service, and will have significant latency.

        Args:
          stream: Whether to stream the tuples back as a stream of JSON server-sent events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/documents/{id}/tuples",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, tuple_list_params.TupleListParams),
            ),
            cast_to=NoneType,
        )


class AsyncTuplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTuplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTuplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#with_streaming_response
        """
        return AsyncTuplesResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Extract tuples from a document by its ID.

        If streaming is enabled, the response
        will be a stream of tuples as JSON server-sent events. This endpoint requires
        calling our external inference service, and will have significant latency.

        Args:
          stream: Whether to stream the tuples back as a stream of JSON server-sent events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/documents/{id}/tuples",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"stream": stream}, tuple_list_params.TupleListParams),
            ),
            cast_to=NoneType,
        )


class TuplesResourceWithRawResponse:
    def __init__(self, tuples: TuplesResource) -> None:
        self._tuples = tuples

        self.list = to_raw_response_wrapper(
            tuples.list,
        )


class AsyncTuplesResourceWithRawResponse:
    def __init__(self, tuples: AsyncTuplesResource) -> None:
        self._tuples = tuples

        self.list = async_to_raw_response_wrapper(
            tuples.list,
        )


class TuplesResourceWithStreamingResponse:
    def __init__(self, tuples: TuplesResource) -> None:
        self._tuples = tuples

        self.list = to_streamed_response_wrapper(
            tuples.list,
        )


class AsyncTuplesResourceWithStreamingResponse:
    def __init__(self, tuples: AsyncTuplesResource) -> None:
        self._tuples = tuples

        self.list = async_to_streamed_response_wrapper(
            tuples.list,
        )
