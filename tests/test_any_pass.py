from typing import Callable, List

from functasticpy.any_pass import any_pass
from functasticpy.stubs.pipe import pipe_sync


def is_divisible_by_3(x: int) -> bool:
    return x % 3 == 0


def is_divisible_by_4(x: int) -> bool:
    return x % 4 == 0


def test_any_pass_data_first() -> None:
    fns: List[Callable[[int], bool]] = [is_divisible_by_3, is_divisible_by_4]

    result = any_pass(12, fns)
    assert result is True

    result = any_pass(8, fns)
    assert result is True

    result = any_pass(7, fns)
    assert result is False


def test_any_pass_data_last() -> None:
    fns: List[Callable[[int], bool]] = [is_divisible_by_3, is_divisible_by_4]

    curried_fn = any_pass(fns)

    result = curried_fn(12)
    assert result is True

    result = curried_fn(8)
    assert result is True

    result = curried_fn(7)
    assert result is False


def test_any_pass_with_empty_functions() -> None:
    fns: List[Callable[[int], bool]] = []

    curried_fn = any_pass(fns)
    result = curried_fn(12)
    assert result is False

    result = curried_fn(0)
    assert result is False


def test_any_pass_with_single_function() -> None:
    fns: List[Callable[[int], bool]] = [is_divisible_by_3]

    result = any_pass(9, fns)
    assert result is True

    result = any_pass(8, fns)
    assert result is False

    curried_fn = any_pass(fns)
    result = curried_fn(6)
    assert result is True


def test_any_pass_in_pipe() -> None:
    fns: List[Callable[[int], bool]] = [is_divisible_by_3, is_divisible_by_4]

    result = pipe_sync(12, any_pass(fns))
    assert result is True

    result = pipe_sync(8, any_pass(fns))
    assert result is True

    result = pipe_sync(7, any_pass(fns))
    assert result is False
