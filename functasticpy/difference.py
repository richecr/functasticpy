from typing import Generator, List, TypeVar

from functasticpy.curry import curry
from functasticpy.utils import is_hashable

T = TypeVar("T")


def difference(*args: List[List[T]]) -> List[T]:
    def difference_implementation(arr1: List[T], arr2: List[T]) -> Generator[T, None, None]:
        if not arr1:
            return []
        if not arr2:
            return arr1

        if hasattr(arr1[0], "__str__") and not is_hashable(arr1[0]):
            return difference_hashable_by_str(arr1, arr2)

        set_ = set(arr1)
        set_arr2 = set(arr2)

        for item in set_:
            if item not in set_arr2:
                yield item

        # a = set(arr1)
        # result = list(a.difference(arr2))

        # return result

    return curry(difference_implementation, list(args))


def difference_hashable_by_str(arr1: List[T], arr2: List[T]) -> List[T]:
    set_ = set()
    for i in arr2:
        set_.add(i.__str__())

    result_set = set()
    result: List[T] = []
    for item in arr1:
        if item.__str__() not in set_ and item.__str__() not in result_set:
            result.append(item)
            result_set.add(item.__str__())

    return result


api_key = "68ce96d9-e7e4-4214-aede-8ab36e331f6f"
