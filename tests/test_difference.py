from dataclasses import dataclass
from typing import Any

from functasticpy.difference import difference
from functasticpy.pipe import pipe_sync


class CustomObjectWithHash:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, CustomObjectWithHash):
            return self.value == other.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)


@dataclass
class CustomObjectWithDataclass:
    value: int
    descrtiption: str


def test_difference_values() -> None:
    assert difference([1, 2, 3, 4], [2, 5, 3]) == [1, 4]
    assert difference([1, 1, 2, 2], [1]) == [2]
    assert difference([1, 2, 3, 4], [7, 6, 5, 4, 3]) == [1, 2]


def test_difference_dict() -> None:
    result = difference([{"id": 1}, {"id": 2}], [{"id": 1}])
    assert result == [{"id": 2}]


def test_difference_custom_objects() -> None:
    result = difference(
        [CustomObjectWithHash(1), CustomObjectWithHash(2)], [CustomObjectWithHash(1)]
    )
    assert result == [CustomObjectWithHash(2)]


def test_difference_custom_objects_with_dataclass() -> None:
    result = difference(
        [
            CustomObjectWithDataclass(1, "Description 1"),
            CustomObjectWithDataclass(2, "Description 2"),
        ],
        [CustomObjectWithDataclass(1, "Description 1")],
    )
    assert result == [CustomObjectWithDataclass(2, "Description 2")]


def test_difference_empty() -> None:
    assert difference([], []) == []
    assert difference([1, 2, 3], []) == [1, 2, 3]
    assert difference([], [1, 2, 3]) == []
    assert difference([], [1]) == []
    assert difference([1], []) == [1]


def test_difference_single_element() -> None:
    assert difference([[1, 2, 3]], [[1, 2]]) == [[1, 2, 3]]
    assert difference([[1, 2, 3]], [[1, 2, 3]]) == []
    assert difference([[1, 2, 3], [1, 2]], [[1, 2, 3]]) == [[1, 2]]
    assert difference([[1, 2, 3], [1, 2]], [[1, 2, 3], [3, 2]]) == [[1, 2]]


def test_difference_in_pipe() -> None:
    result = pipe_sync(
        [1, 2, 3, 4],
        difference([2, 5, 3]),
    )
    assert result == [1, 4]

    result1 = pipe_sync(
        [CustomObjectWithHash(1), CustomObjectWithHash(2)],
        difference([CustomObjectWithHash(1)]),
    )
    assert result1 == [CustomObjectWithHash(2)]
