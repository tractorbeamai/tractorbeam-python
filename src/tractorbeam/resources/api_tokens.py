# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import api_token_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_token import APIToken
from ..types.api_token_list_response import APITokenListResponse

__all__ = ["APITokensResource", "AsyncAPITokensResource"]


class APITokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APITokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return APITokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APITokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#with_streaming_response
        """
        return APITokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIToken:
        """
        Create a new API token for the authenticated organization.

        Args:
          name: The name that will be used to identify the API token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api-tokens",
            body=maybe_transform({"name": name}, api_token_create_params.APITokenCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIToken:
        """Get an API token by its ID (e.g.

        `token_123`). The token must belong to the
        authenticated user's organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api-tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APITokenListResponse:
        """List all API tokens for the authenticated user's organization."""
        return self._get(
            "/api-tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APITokenListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revoke a specific API Token for the authenticated organization.

        After
        revocation, the token will no longer be valid and cannot be used to authenticate
        requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api-tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAPITokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPITokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPITokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPITokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tractorbeamai/tractorbeam-python#with_streaming_response
        """
        return AsyncAPITokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIToken:
        """
        Create a new API token for the authenticated organization.

        Args:
          name: The name that will be used to identify the API token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api-tokens",
            body=await async_maybe_transform({"name": name}, api_token_create_params.APITokenCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIToken:
        """Get an API token by its ID (e.g.

        `token_123`). The token must belong to the
        authenticated user's organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api-tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APITokenListResponse:
        """List all API tokens for the authenticated user's organization."""
        return await self._get(
            "/api-tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APITokenListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revoke a specific API Token for the authenticated organization.

        After
        revocation, the token will no longer be valid and cannot be used to authenticate
        requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api-tokens/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class APITokensResourceWithRawResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = to_raw_response_wrapper(
            api_tokens.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            api_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            api_tokens.delete,
        )


class AsyncAPITokensResourceWithRawResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = async_to_raw_response_wrapper(
            api_tokens.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            api_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_tokens.delete,
        )


class APITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = to_streamed_response_wrapper(
            api_tokens.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            api_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_tokens.delete,
        )


class AsyncAPITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = async_to_streamed_response_wrapper(
            api_tokens.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            api_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_tokens.delete,
        )
