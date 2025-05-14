from typing import Callable, List, TypeVar, Union

T = TypeVar("T")


def curry(
    fn: Callable, args: List[Union[T, List[Callable[[T], bool]]]]
) -> Union[bool, Callable[[T], bool]]:
    diff = fn.__code__.co_argcount - len(args)

    if diff == 0:
        return fn(*args)
    elif diff == 1:
        return lambda data: fn(data, *args)
    else:
        raise ValueError("Wrong number of arguments")
