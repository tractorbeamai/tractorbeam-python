# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam
from tractorbeam.types import (
    Graph,
    GraphListResponse,
    GraphQueryResponse,
    GraphTuplesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraphs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Tractorbeam) -> None:
        graph = client.graphs.create(
            name="name",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Tractorbeam) -> None:
        graph = client.graphs.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.graphs.with_raw_response.retrieve(
                name="my_graph",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.graphs.with_raw_response.retrieve(
                name="",
                owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
            )

    @parametrize
    def test_method_list(self, client: Tractorbeam) -> None:
        graph = client.graphs.list()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphListResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Tractorbeam) -> None:
        graph = client.graphs.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )
        assert graph is None

    @parametrize
    def test_raw_response_delete(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert graph is None

    @parametrize
    def test_streaming_response_delete(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert graph is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.graphs.with_raw_response.delete(
                name="my_graph",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.graphs.with_raw_response.delete(
                name="",
                owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
            )

    @parametrize
    def test_method_query(self, client: Tractorbeam) -> None:
        graph = client.graphs.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        )
        assert_matches_type(GraphQueryResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphQueryResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphQueryResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.graphs.with_raw_response.query(
                name="graph-name",
                owner="",
                sparql="sparql",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.graphs.with_raw_response.query(
                name="",
                owner="graph-owner",
                sparql="sparql",
            )

    @parametrize
    def test_method_tuples(self, client: Tractorbeam) -> None:
        graph = client.graphs.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        )
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    def test_method_tuples_with_all_params(self, client: Tractorbeam) -> None:
        graph = client.graphs.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
            embeddings=[[0]],
        )
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_tuples(self, client: Tractorbeam) -> None:
        response = client.graphs.with_raw_response.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_tuples(self, client: Tractorbeam) -> None:
        with client.graphs.with_streaming_response.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphTuplesResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tuples(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.graphs.with_raw_response.tuples(
                name="graph-name",
                owner="",
                tuples=[
                    {
                        "object": "Tractorbeam",
                        "predicate": "works_at",
                        "subject": "Wade",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.graphs.with_raw_response.tuples(
                name="",
                owner="graph-owner",
                tuples=[
                    {
                        "object": "Tractorbeam",
                        "predicate": "works_at",
                        "subject": "Wade",
                    }
                ],
            )


class TestAsyncGraphs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.create(
            name="name",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.retrieve(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.graphs.with_raw_response.retrieve(
                name="my_graph",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.graphs.with_raw_response.retrieve(
                name="",
                owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.list()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphListResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )
        assert graph is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert graph is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.delete(
            name="my_graph",
            owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert graph is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.graphs.with_raw_response.delete(
                name="my_graph",
                owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.graphs.with_raw_response.delete(
                name="",
                owner="org_2nlswGH0pZ1V1OlHYAUwQG6TVBx",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        )
        assert_matches_type(GraphQueryResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphQueryResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.query(
            name="graph-name",
            owner="graph-owner",
            sparql="sparql",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphQueryResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.graphs.with_raw_response.query(
                name="graph-name",
                owner="",
                sparql="sparql",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.graphs.with_raw_response.query(
                name="",
                owner="graph-owner",
                sparql="sparql",
            )

    @parametrize
    async def test_method_tuples(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        )
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    async def test_method_tuples_with_all_params(self, async_client: AsyncTractorbeam) -> None:
        graph = await async_client.graphs.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
            embeddings=[[0]],
        )
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_tuples(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.with_raw_response.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphTuplesResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_tuples(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.with_streaming_response.tuples(
            name="graph-name",
            owner="graph-owner",
            tuples=[
                {
                    "object": "Tractorbeam",
                    "predicate": "works_at",
                    "subject": "Wade",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphTuplesResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tuples(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.graphs.with_raw_response.tuples(
                name="graph-name",
                owner="",
                tuples=[
                    {
                        "object": "Tractorbeam",
                        "predicate": "works_at",
                        "subject": "Wade",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.graphs.with_raw_response.tuples(
                name="",
                owner="graph-owner",
                tuples=[
                    {
                        "object": "Tractorbeam",
                        "predicate": "works_at",
                        "subject": "Wade",
                    }
                ],
            )
