import asyncio

import pytest

from functasticpy.pipe import pipe, pipe_sync


async def async_increment(x: int) -> int:
    await asyncio.sleep(0.00001)
    return x + 1


def sync_multiply(x: int) -> int:
    return x * 2


async def async_add(x: int) -> int:
    await asyncio.sleep(0.00001)
    return x + 3


@pytest.mark.asyncio
async def test_pipe_with_async_function() -> None:
    result = await pipe(5, async_increment)
    assert result == 6


@pytest.mark.asyncio
async def test_pipe_with_sync_function() -> None:
    result = await pipe(5, sync_multiply)
    assert result == 10


@pytest.mark.asyncio
async def test_pipe_with_combined_functions() -> None:
    result = await pipe(5, async_increment, sync_multiply)
    assert result == 12


@pytest.mark.asyncio
async def test_pipe_with_multiple_async_functions() -> None:
    result = await pipe(5, async_increment, async_add)
    assert result == 9


@pytest.mark.asyncio
async def test_pipe_with_mixed_functions() -> None:
    result = await pipe(5, async_increment, sync_multiply, async_add)
    assert result == 15


def test_pipe_sync_with_sync_function() -> None:
    result = pipe_sync(5, sync_multiply)
    assert result == 10
