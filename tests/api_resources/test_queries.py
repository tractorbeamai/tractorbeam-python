# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam
from tractorbeam.types import QueryDecodeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_decode(self, client: Tractorbeam) -> None:
        query = client.queries.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        )
        assert_matches_type(QueryDecodeResponse, query, path=["response"])

    @parametrize
    def test_raw_response_decode(self, client: Tractorbeam) -> None:
        response = client.queries.with_raw_response.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryDecodeResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_decode(self, client: Tractorbeam) -> None:
        with client.queries.with_streaming_response.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryDecodeResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_decode(self, async_client: AsyncTractorbeam) -> None:
        query = await async_client.queries.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        )
        assert_matches_type(QueryDecodeResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_decode(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.queries.with_raw_response.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryDecodeResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_decode(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.queries.with_streaming_response.decode(
            depth=0,
            graph_names=["string"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryDecodeResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True
