from __future__ import annotations

from typing import Callable, Mapping, Optional, TypeVar, overload

K = TypeVar("K")
V = TypeVar("V")

@overload
def prop(key: K) -> Callable[[Mapping[K, V] | None], Optional[V]]: ...
@overload
def prop(key: K, obj: Mapping[K, V] | None) -> Optional[V]: ...
