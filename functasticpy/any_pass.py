from typing import Any, Callable, Iterable


def any_pass(predicates: Iterable[Callable[..., Any]]):
    def checker(value: Any) -> bool:
        for predicate in predicates:
            if predicate(value):
                return True
        return False

    return checker
