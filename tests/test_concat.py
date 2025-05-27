from functasticpy.concat import concat


def test_concat_data_first() -> None:
    result = concat([1, 2], [3, 4])
    assert result == [1, 2, 3, 4]

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
