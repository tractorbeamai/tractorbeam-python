# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam
from tractorbeam.types import DocumentContents

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tractorbeam) -> None:
        content = client.documents.contents.retrieve(
            "id",
        )
        assert_matches_type(DocumentContents, content, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tractorbeam) -> None:
        response = client.documents.contents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(DocumentContents, content, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tractorbeam) -> None:
        with client.documents.contents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(DocumentContents, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.contents.with_raw_response.retrieve(
                "",
            )


class TestAsyncContents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTractorbeam) -> None:
        content = await async_client.documents.contents.retrieve(
            "id",
        )
        assert_matches_type(DocumentContents, content, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.contents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(DocumentContents, content, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.contents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(DocumentContents, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.contents.with_raw_response.retrieve(
                "",
            )
