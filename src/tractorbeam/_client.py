# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_query_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import graphs, queries, api_tokens
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TractorbeamError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.documents import documents
from .types.query_response import QueryResponse
from .types.health_check_response import HealthCheckResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Tractorbeam",
    "AsyncTractorbeam",
    "Client",
    "AsyncClient",
]


class Tractorbeam(SyncAPIClient):
    api_tokens: api_tokens.APITokensResource
    documents: documents.DocumentsResource
    graphs: graphs.GraphsResource
    queries: queries.QueriesResource
    with_raw_response: TractorbeamWithRawResponse
    with_streaming_response: TractorbeamWithStreamedResponse

    # client options
    api_token: str

    def __init__(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous tractorbeam client instance.

        This automatically infers the `api_token` argument from the `API_TOKEN` environment variable if it is not provided.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
        if api_token is None:
            raise TractorbeamError(
                "The api_token client option must be set either by passing api_token to the client or by setting the API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = os.environ.get("TRACTORBEAM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.tractorbeam.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_tokens = api_tokens.APITokensResource(self)
        self.documents = documents.DocumentsResource(self)
        self.graphs = graphs.GraphsResource(self)
        self.queries = queries.QueriesResource(self)
        self.with_raw_response = TractorbeamWithRawResponse(self)
        self.with_streaming_response = TractorbeamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_token=api_token or self.api_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCheckResponse:
        """This is a simple health check that does not require authentication.

        It is used
        to check if the server is running and healthy.
        """
        return self.get(
            "/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthCheckResponse,
        )

    def query(
        self,
        *,
        depth: int,
        graph_names: List[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryResponse:
        """
        Execute a natural language query across multiple graphs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/query",
            body=maybe_transform(
                {
                    "depth": depth,
                    "graph_names": graph_names,
                    "query": query,
                },
                client_query_params.ClientQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTractorbeam(AsyncAPIClient):
    api_tokens: api_tokens.AsyncAPITokensResource
    documents: documents.AsyncDocumentsResource
    graphs: graphs.AsyncGraphsResource
    queries: queries.AsyncQueriesResource
    with_raw_response: AsyncTractorbeamWithRawResponse
    with_streaming_response: AsyncTractorbeamWithStreamedResponse

    # client options
    api_token: str

    def __init__(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async tractorbeam client instance.

        This automatically infers the `api_token` argument from the `API_TOKEN` environment variable if it is not provided.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
        if api_token is None:
            raise TractorbeamError(
                "The api_token client option must be set either by passing api_token to the client or by setting the API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = os.environ.get("TRACTORBEAM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.tractorbeam.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_tokens = api_tokens.AsyncAPITokensResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.graphs = graphs.AsyncGraphsResource(self)
        self.queries = queries.AsyncQueriesResource(self)
        self.with_raw_response = AsyncTractorbeamWithRawResponse(self)
        self.with_streaming_response = AsyncTractorbeamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_token=api_token or self.api_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthCheckResponse:
        """This is a simple health check that does not require authentication.

        It is used
        to check if the server is running and healthy.
        """
        return await self.get(
            "/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthCheckResponse,
        )

    async def query(
        self,
        *,
        depth: int,
        graph_names: List[str],
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryResponse:
        """
        Execute a natural language query across multiple graphs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/query",
            body=await async_maybe_transform(
                {
                    "depth": depth,
                    "graph_names": graph_names,
                    "query": query,
                },
                client_query_params.ClientQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TractorbeamWithRawResponse:
    def __init__(self, client: Tractorbeam) -> None:
        self.api_tokens = api_tokens.APITokensResourceWithRawResponse(client.api_tokens)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.graphs = graphs.GraphsResourceWithRawResponse(client.graphs)
        self.queries = queries.QueriesResourceWithRawResponse(client.queries)

        self.health_check = to_raw_response_wrapper(
            client.health_check,
        )
        self.query = to_raw_response_wrapper(
            client.query,
        )


class AsyncTractorbeamWithRawResponse:
    def __init__(self, client: AsyncTractorbeam) -> None:
        self.api_tokens = api_tokens.AsyncAPITokensResourceWithRawResponse(client.api_tokens)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.graphs = graphs.AsyncGraphsResourceWithRawResponse(client.graphs)
        self.queries = queries.AsyncQueriesResourceWithRawResponse(client.queries)

        self.health_check = async_to_raw_response_wrapper(
            client.health_check,
        )
        self.query = async_to_raw_response_wrapper(
            client.query,
        )


class TractorbeamWithStreamedResponse:
    def __init__(self, client: Tractorbeam) -> None:
        self.api_tokens = api_tokens.APITokensResourceWithStreamingResponse(client.api_tokens)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.graphs = graphs.GraphsResourceWithStreamingResponse(client.graphs)
        self.queries = queries.QueriesResourceWithStreamingResponse(client.queries)

        self.health_check = to_streamed_response_wrapper(
            client.health_check,
        )
        self.query = to_streamed_response_wrapper(
            client.query,
        )


class AsyncTractorbeamWithStreamedResponse:
    def __init__(self, client: AsyncTractorbeam) -> None:
        self.api_tokens = api_tokens.AsyncAPITokensResourceWithStreamingResponse(client.api_tokens)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.graphs = graphs.AsyncGraphsResourceWithStreamingResponse(client.graphs)
        self.queries = queries.AsyncQueriesResourceWithStreamingResponse(client.queries)

        self.health_check = async_to_streamed_response_wrapper(
            client.health_check,
        )
        self.query = async_to_streamed_response_wrapper(
            client.query,
        )


Client = Tractorbeam

AsyncClient = AsyncTractorbeam
