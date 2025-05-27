from typing import Callable, Dict, List, TypeVar, Union

from functasticpy.curry import curry

T = TypeVar("T")
U = TypeVar("U")


def count_by(*args: Union[List[T], Callable[[T], U]]) -> Dict[U, int]:
    def count_by_implementation(arr: List[T], fn: Callable[[T], U]) -> Dict[U, int]:
        result: Dict[U, int] = {}
        for item in arr:
            key = fn(item)
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
        return result

    return curry(count_by_implementation, list(args))
