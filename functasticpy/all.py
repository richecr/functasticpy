# all.py
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def all(predicate: Callable[[T], bool]) -> Callable[[Sequence[T]], bool]:
    def checker(items: Sequence[T]) -> bool:
        for item in items:
            if not predicate(item):
                return False
        return True

    return checker
