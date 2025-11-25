from functasticpy.concat import concat
from functasticpy.stubs.pipe import pipe_sync


def test_concat_data_first() -> None:
    result1 = concat([1, 2], [3, 4])
    assert result1 == [1, 2, 3, 4]

    result = concat([5, 6], [7, 8])
    assert result == [5, 6, 7, 8]


def test_concat_data_last() -> None:
    curried_fn = concat([3, 4])

    result = curried_fn([1, 2])
    assert result == [1, 2, 3, 4]

    curried_fn = concat([7, 8])
    result = curried_fn([5, 6])
    assert result == [5, 6, 7, 8]


def test_concat_with_empty_lists() -> None:
    result = concat([], [1, 2])
    assert result == [1, 2]

    result = concat([], [])
    assert result == []

    curried_fn = concat([3, 4])
    result = curried_fn([])
    assert result == [3, 4]


def test_concat_with_single_element() -> None:
    result = concat([1], [2])
    assert result == [1, 2]

    result = concat([3], [])
    assert result == [3]

    curried_fn = concat([5])
    result = curried_fn([4])
    assert result == [4, 5]


def test_concat_with_multiple_elements() -> None:
    result = concat([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]

    result = concat([7, 8], [9])
    assert result == [7, 8, 9]

    curried_fn = concat([12, 13])
    result = curried_fn([10, 11])
    assert result == [10, 11, 12, 13]


def test_concat_with_nested_lists() -> None:
    result = concat([[1, 2], [3, 4]], [[5, 6]])
    assert result == [[1, 2], [3, 4], [5, 6]]

    result = concat([[7]], [[8, 9]])
    assert result == [[7], [8, 9]]

    curried_fn = concat([[10]])
    result = curried_fn([[11], [12]])
    assert result == [[11], [12], [10]]


def test_concat_with_list_str() -> None:
    result = concat(["Hello, "], ["World!"])
    assert result == ["Hello, ", "World!"]


def test_concat_with_strings() -> None:
    result1 = concat("Hello, ", "World!")
    assert result1 == "Hello, World!"


def test_concat_in_pipe() -> None:
    result = pipe_sync([1, 2], concat([3, 4]), concat([5, 6]))
    assert result == [1, 2, 3, 4, 5, 6]
