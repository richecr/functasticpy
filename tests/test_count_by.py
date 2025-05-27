from typing import List

from functasticpy.count_by import count_by


def to_lower_case(x: str) -> str:
    return x.lower()


def get_first_letter(x: str) -> str:
    return x[0].lower() if x else ""


def test_count_by_data_first() -> None:
    data = ["a", "b", "c", "B", "A", "a"]
    result = count_by(data, to_lower_case)
    assert result == {"a": 3, "b": 2, "c": 1}

    data = ["apple", "banana", "apple", "orange", "banana"]
    result = count_by(data, lambda x: x[0])
    assert result == {"a": 2, "b": 2, "o": 1}


def test_count_by_data_last() -> None:
    data = ["a", "b", "c", "B", "A", "a"]
    curried_fn = count_by(to_lower_case)
    result = curried_fn(data)
    assert result == {"a": 3, "b": 2, "c": 1}

    data = ["apple", "banana", "apple", "orange", "banana"]
    curried_fn = count_by(get_first_letter)
    result = curried_fn(data)
    assert result == {"a": 2, "b": 2, "o": 1}


def test_count_by_with_empty_list() -> None:
    data: List[str] = []
    result = count_by(data, to_lower_case)
    assert result == {}

    curried_fn = count_by(to_lower_case)
    result = curried_fn(data)
    assert result == {}


def test_count_by_with_single_item() -> None:
    data = ["a"]
    result = count_by(data, to_lower_case)
    assert result == {"a": 1}

    curried_fn = count_by(to_lower_case)
    result = curried_fn(data)
    assert result == {"a": 1}
