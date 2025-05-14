from typing import Callable, List, TypeVar, overload

T = TypeVar("T")

@overload
def all_pass(value: T, functions: List[Callable[[T], bool]]) -> bool: ...
@overload
def all_pass(functions: List[Callable[[T], bool]]) -> Callable[[T], bool]: ...
