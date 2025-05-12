from typing import Awaitable, Callable, TypeVar, Union

T = TypeVar("T")


async def pipe(value: T, *functions: Callable[[T], Union[T, Awaitable[T]]]) -> T:
    for func in functions:
        result = func(value)
        if isinstance(result, Awaitable):
            value = await result
        else:
            value = result
    return value
