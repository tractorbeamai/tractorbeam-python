# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraphs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Tractorbeam) -> None:
        graph = client.graphs.create(
            body={},
        )
        assert_matches_type(object, graph, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(object, graph, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(object, graph, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGraphs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.create(
            body={},
        )
        assert_matches_type(object, graph, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(object, graph, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(object, graph, path=["response"])

        assert cast(Any, response.is_closed) is True
