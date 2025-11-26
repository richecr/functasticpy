from functasticpy.all import all as all_
from functasticpy.pipe import pipe


def is_positive(n: int) -> bool:
    return n > 0


def test_all__basic_usage() -> None:
    curried_fn = all_(is_positive)

    result = curried_fn([12, 3, 1])
    assert result is True

    result = curried_fn([12, -3, 1])
    assert result is False

    result = curried_fn([-1, -2, -3])
    assert result is False


def test_all__with_empty_array() -> None:
    curried_fn = all_(is_positive)
    result = curried_fn([])
    assert result is True


def test_all__in_pipe() -> None:
    result = pipe([12, 3, 1], all_(is_positive))
    assert result is True

    result = pipe([12, -3, 1], all_(is_positive))
    assert result is False

    result = pipe([-1, -3, -2], all_(is_positive))
    assert result is False
