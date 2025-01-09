# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tractorbeam import Tractorbeam, AsyncTractorbeam
from tractorbeam.types.graphs import TupleCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTuples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Tractorbeam) -> None:
        tuple_ = client.graphs.tuples.create(
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
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Tractorbeam) -> None:
        tuple_ = client.graphs.tuples.create(
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
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Tractorbeam) -> None:
        response = client.graphs.tuples.with_raw_response.create(
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
        tuple_ = response.parse()
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Tractorbeam) -> None:
        with client.graphs.tuples.with_streaming_response.create(
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

            tuple_ = response.parse()
            assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Tractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.graphs.tuples.with_raw_response.create(
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
            client.graphs.tuples.with_raw_response.create(
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


class TestAsyncTuples:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTractorbeam) -> None:
        tuple_ = await async_client.graphs.tuples.create(
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
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTractorbeam) -> None:
        tuple_ = await async_client.graphs.tuples.create(
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
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTractorbeam) -> None:
        response = await async_client.graphs.tuples.with_raw_response.create(
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
        tuple_ = await response.parse()
        assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTractorbeam) -> None:
        async with async_client.graphs.tuples.with_streaming_response.create(
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

            tuple_ = await response.parse()
            assert_matches_type(TupleCreateResponse, tuple_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncTractorbeam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.graphs.tuples.with_raw_response.create(
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
            await async_client.graphs.tuples.with_raw_response.create(
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
