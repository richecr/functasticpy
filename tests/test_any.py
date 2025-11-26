from functasticpy.any import any as any_
from functasticpy.pipe import pipe


def is_positive(n: int) -> bool:
    return n > 0


def test_any__basic_usage() -> None:
    curried_fn = any_(is_positive)

    result = curried_fn([12, -3, 0])
    assert result is True

    result = curried_fn([-1, -2, -3])
    assert result is False


def test_any__with_empty_array() -> None:
    curried_fn = any_(is_positive)
    result = curried_fn([])
    assert result is False


def test_any__in_pipe() -> None:
    result = pipe([12, -3, 0], any_(is_positive))
    assert result is True

    result = pipe([8, -3, 0], any_(is_positive))
    assert result is True

    result = pipe([-1, -3, -2], any_(is_positive))
    assert result is False
