from typing import Awaitable, Callable, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


async def pipe(value: T, *functions: Callable) -> T:
    for func in functions:
        result = func(value)
        if isinstance(result, Awaitable):
            value = await result
        else:
            value = result
    return value


def pipe_sync(value: T, *functions: Callable[[T], Union[T]]) -> T:
    for func in functions:
        result = func(value)

    return result
