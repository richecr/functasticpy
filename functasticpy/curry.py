from typing import Any, Callable, TypeVar

T = TypeVar("T")


def curry(fn: Callable, args: list[T]) -> Any:
    diff = fn.__code__.co_argcount - len(args)

    if diff == 0:
        return fn(*args)
    elif diff == 1:
        return lambda data: fn(data, *args)
    else:
        raise ValueError("Wrong number of arguments")
