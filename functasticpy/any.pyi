from __future__ import annotations

from typing import Callable, Sequence, TypeVar

T = TypeVar("T")

def any(predicate: Callable[[T], bool]) -> Callable[[Sequence[T]], bool]: ...
