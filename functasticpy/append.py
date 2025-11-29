# append.py
from __future__ import annotations

from typing import Callable, List, Sequence, TypeVar

T = TypeVar("T")


def append(el: T) -> Callable[[Sequence[T]], List[T]]:
    def inner(lst: Sequence[T]) -> List[T]:
        return list(lst) + [el]

    return inner
