from typing import List, TypeVar

from functasticpy.curry import curry

T = TypeVar("T")


def concat(*args: List[List[T]]) -> List[T]:
    def concat_implementation(arr1: List[T], arr2: List[T]) -> List[T]:
        return arr1 + arr2

    return curry(concat_implementation, list(args))
