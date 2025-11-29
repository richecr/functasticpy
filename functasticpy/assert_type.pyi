from __future__ import annotations

from typing import Callable, TypeGuard, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def assert_type(predicate: Callable[[T], TypeGuard[U]]) -> Callable[[T], U]: ...
