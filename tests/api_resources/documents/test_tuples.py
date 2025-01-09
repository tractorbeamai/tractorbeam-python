# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tractorbeam import Tractorbeam, AsyncTractorbeam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTuples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tractorbeam) -> None:
        tuple_ = client.documents.tuples.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )
        assert tuple_ is None

    @parametrize
    def test_method_list_with_all_params(self, client: Tractorbeam) -> None:
        tuple_ = client.documents.tuples.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
            stream=True,
        )
        assert tuple_ is None

    @parametrize
    def test_raw_response_list(self, client: Tractorbeam) -> None:
        response = client.documents.tuples.with_raw_response.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tuple_ = response.parse()
        assert tuple_ is None

    @parametrize
    def test_streaming_response_list(self, client: Tractorbeam) -> None:
        with client.documents.tuples.with_streaming_response.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tuple_ = response.parse()
            assert tuple_ is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.tuples.with_raw_response.list(
                id="",
            )


class TestAsyncTuples:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTractorbeam) -> None:
        tuple_ = await async_client.documents.tuples.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )
        assert tuple_ is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTractorbeam) -> None:
        tuple_ = await async_client.documents.tuples.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
            stream=True,
        )
        assert tuple_ is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.tuples.with_raw_response.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tuple_ = await response.parse()
        assert tuple_ is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.tuples.with_streaming_response.list(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tuple_ = await response.parse()
            assert tuple_ is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.tuples.with_raw_response.list(
                id="",
            )
