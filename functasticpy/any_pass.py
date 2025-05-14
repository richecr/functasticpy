from typing import Callable, List, TypeVar, Union

from functasticpy.curry import curry

T = TypeVar("T")


def any_pass(
    *args: Union[T, List[Callable[[T], bool]]],
) -> Union[bool, Callable[[T], bool]]:
    def any_pass_implementation(data: T, fns: List[Callable[[T], bool]]) -> bool:
        return any(fn(data) for fn in fns)

    return curry(any_pass_implementation, list(args))
