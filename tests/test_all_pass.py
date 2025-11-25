from typing import Callable, List

from functasticpy.all_pass import all_pass
from functasticpy.pipe import pipe


def is_divisible_by_3(x: int) -> bool:
    return x % 3 == 0


def is_divisible_by_4(x: int) -> bool:
    return x % 4 == 0


def test_all_pass_return_true() -> None:
    fns = [is_divisible_by_3, is_divisible_by_4]

    curried_fn = all_pass(fns)
    result = curried_fn(12)
    assert result is True


def test_all_pass_return_false() -> None:
    fns = [is_divisible_by_3, is_divisible_by_4]

    curried_fn = all_pass(fns)

    result = curried_fn(8)
    assert result is False


def test_all_pass_with_empty_functions() -> None:
    fns: List[Callable[[int], bool]] = []

    curried_fn = all_pass(fns)
    result = curried_fn(12)
    assert result is True


def test_all_pass_with_single_function() -> None:
    fns = [is_divisible_by_3]

    curried_fn = all_pass(fns)
    result = curried_fn(9)
    assert result is True

    curried_fn = all_pass(fns)
    result = curried_fn(8)
    assert result is False

    curried_fn = all_pass(fns)
    result = curried_fn(6)
    assert result is True


def test_all_pass_with_pipe() -> None:
    fns = [is_divisible_by_3, is_divisible_by_4]

    curried_fn = all_pass(fns)
    result = curried_fn(pipe(6, lambda x: x + 6))
    assert result is True

    result = curried_fn(pipe(7, lambda x: x + 1))
    assert result is False
