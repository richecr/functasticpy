# any.py
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def any(predicate: Callable[[T], bool]) -> Callable[[Sequence[T]], bool]:
    def checker(items: Sequence[T]) -> bool:
        for item in items:
            if predicate(item):
                return True
        return False

    return checker
