from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


def all_pass(predicates: Iterable[Callable[[T], bool]]) -> Callable[[T], bool]:
    return lambda value: all(predicate(value) for predicate in predicates)
