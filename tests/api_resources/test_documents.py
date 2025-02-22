# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam
from tractorbeam.types import Document, DocumentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Tractorbeam) -> None:
        document = client.documents.create(
            name="my_document.txt",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Tractorbeam) -> None:
        document = client.documents.create(
            name="my_document.txt",
            file=[0],
            text="Hello world",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.create(
            name="my_document.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.create(
            name="my_document.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Tractorbeam) -> None:
        document = client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Tractorbeam) -> None:
        document = client.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_contents(self, client: Tractorbeam) -> None:
        document = client.documents.contents(
            "id",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_contents(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.contents(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_contents(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.contents(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_contents(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.contents(
                "",
            )

    @parametrize
    def test_method_get(self, client: Tractorbeam) -> None:
        document = client.documents.get(
            "id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_tuples(self, client: Tractorbeam) -> None:
        document = client.documents.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )
        assert document is None

    @parametrize
    def test_method_tuples_with_all_params(self, client: Tractorbeam) -> None:
        document = client.documents.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
            stream=True,
            target_graph_name="target_graph_name",
            target_graph_owner="target_graph_owner",
        )
        assert document is None

    @parametrize
    def test_raw_response_tuples(self, client: Tractorbeam) -> None:
        response = client.documents.with_raw_response.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_tuples(self, client: Tractorbeam) -> None:
        with client.documents.with_streaming_response.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tuples(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.tuples(
                id="",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.create(
            name="my_document.txt",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.create(
            name="my_document.txt",
            file=[0],
            text="Hello world",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.create(
            name="my_document.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.create(
            name="my_document.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_contents(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.contents(
            "id",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_contents(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.contents(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_contents(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.contents(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_contents(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.contents(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.get(
            "id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_tuples(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )
        assert document is None

    @parametrize
    async def test_method_tuples_with_all_params(self, async_client: AsyncTractorbeam) -> None:
        document = await async_client.documents.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
            stream=True,
            target_graph_name="target_graph_name",
            target_graph_owner="target_graph_owner",
        )
        assert document is None

    @parametrize
    async def test_raw_response_tuples(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.documents.with_raw_response.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_tuples(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.documents.with_streaming_response.tuples(
            id="doc_2yYISEvrO9LrLAOJjnw27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tuples(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.tuples(
                id="",
            )
