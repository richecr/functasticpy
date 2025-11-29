from typing import TypeGuard

import pytest

from functasticpy.assert_type import assert_type


def is_str(x: str) -> TypeGuard[str]:
    return isinstance(x, str)


def is_length_five(x: str) -> TypeGuard[str]:
    return isinstance(x, str) and len(x) == 5


def is_positive(x: int) -> TypeGuard[int]:
    return x > 0


def test_assert_type__basic_usage_with_string() -> None:
    assert_str = assert_type(is_str)

    result = assert_str("hello")
    assert result == "hello"


def test_assert_type__raises_on_wrong_type() -> None:
    is_length_five_fn = assert_type(is_length_five)

    with pytest.raises(AssertionError, match="Type assertion failed"):
        is_length_five_fn("42")


def test_assert_type__raises_on_failed_predicate() -> None:
    assert_positive = assert_type(is_positive)

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_positive(-5)

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_positive(0)


def test_assert_type__successful_predicate() -> None:
    assert_positive = assert_type(is_positive)

    result = assert_positive(10)
    assert result == 10

    result = assert_positive(1)
    assert result == 1


def test_assert_type__with_none() -> None:
    def is_not_none(x: object) -> TypeGuard[object]:
        return x is not None

    assert_not_none = assert_type(is_not_none)

    result = assert_not_none("value")
    assert result == "value"

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_not_none(None)


def test_assert_type__with_complex_predicate() -> None:
    def is_even(x: int) -> TypeGuard[int]:
        return x % 2 == 0

    assert_even = assert_type(is_even)

    result = assert_even(4)
    assert result == 4

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_even(3)


def test_assert_type__with_list_check() -> None:
    def is_list(x: object) -> TypeGuard[list]:
        return isinstance(x, list)

    assert_list = assert_type(is_list)

    result = assert_list([1, 2, 3])
    assert result == [1, 2, 3]

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_list((1, 2, 3))


def test_assert_type__with_empty_values() -> None:
    def is_non_empty_str(x: str) -> TypeGuard[str]:
        return isinstance(x, str) and len(x) > 0

    assert_non_empty = assert_type(is_non_empty_str)

    result = assert_non_empty("hello")
    assert result == "hello"

    with pytest.raises(AssertionError, match="Type assertion failed"):
        assert_non_empty("")
