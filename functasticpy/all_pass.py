from typing import Callable, List, TypeVar, Union

from functasticpy.curry import curry

T = TypeVar("T")


def all_pass(
    *args: Union[T, List[Callable[[T], bool]]],
) -> Union[bool, Callable[[T], bool]]:
    def all_pass_implementation(data: T, fns: List[Callable[[T], bool]]) -> bool:
        return all(fn(data) for fn in fns)

    return curry(all_pass_implementation, list(args))
