from functasticpy.append import append
from functasticpy.pipe import pipe


def test_append__basic_usage() -> None:
    add_four = append(4)

    result = add_four([1, 2, 3])
    assert result == [1, 2, 3, 4]


def test_append__empty_list() -> None:
    add_one = append(1)

    result = add_one([])
    assert result == [1]


def test_append__with_strings() -> None:
    add_world = append("world")

    result = add_world(["hello"])
    assert result == ["hello", "world"]


def test_append__does_not_mutate_original() -> None:
    original = [1, 2, 3]
    add_four = append(4)

    result = add_four(original)

    assert result == [1, 2, 3, 4]
    assert original == [1, 2, 3]  # original unchanged


def test_append__with_tuple_input() -> None:
    add_four = append(4)

    result = add_four((1, 2, 3))
    assert result == [1, 2, 3, 4]
    assert isinstance(result, list)


def test_append__with_different_types() -> None:
    add_none = append(None)
    result = add_none([1, 2])
    assert result == [1, 2, None]

    add_dict = append({"key": "value"})
    result = add_dict([])
    assert result == [{"key": "value"}]

    add_list = append([1, 2])
    result = add_list([[3, 4]])
    assert result == [[3, 4], [1, 2]]


def test_append__multiple_appends() -> None:
    add_one = append(1)
    add_two = append(2)

    result = add_two(add_one([]))
    assert result == [1, 2]


def test_append__in_pipe() -> None:
    result = pipe([1, 2, 3], append(4), append(5))
    assert result == [1, 2, 3, 4, 5]


def test_append__with_large_list() -> None:
    add_hundred = append(100)
    large_list = list(range(50))

    result = add_hundred(large_list)
    assert result == list(range(50)) + [100]
    assert len(result) == 51


def test_append__preserves_duplicates() -> None:
    add_one = append(1)

    result = add_one([1, 1, 1])
    assert result == [1, 1, 1, 1]
