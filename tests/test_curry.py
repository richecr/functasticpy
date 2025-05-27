import pytest

from functasticpy.curry import curry


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def is_even(x: int) -> bool:
    return x % 2 == 0


def test_curry_with_exact_number_of_arguments() -> None:
    result = curry(add, [2, 3])
    assert result == 5

    result = curry(multiply, [2, 3])
    assert result == 6


def test_curry_with_missing_argument() -> None:
    curried_add = curry(add, [2])
    assert curried_add(3) == 5

    curried_multiply = curry(multiply, [2])
    assert curried_multiply(3) == 6


def test_curry_with_extra_arguments() -> None:
    with pytest.raises(ValueError):
        curry(add, [2, 3, 4])

    with pytest.raises(ValueError):
        curry(multiply, [2, 3, 4])


def test_curry_with_single_function_argument() -> None:
    curried_is_even = curry(is_even, [2])
    assert curried_is_even is True

    curried_is_even = curry(is_even, [3])
    assert curried_is_even is False
