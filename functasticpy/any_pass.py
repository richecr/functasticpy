from typing import Any, Callable, Iterable


def any_pass(predicates: Iterable[Callable[..., Any]]):
    """Create a function that checks if a value passes any of multiple predicates.

    Takes multiple predicate functions and returns a checker function that
    returns True if the value satisfies at least one of the predicates.
    Supports TypeGuard for advanced type narrowing when used with proper
    type annotations (see .pyi file).

    Args:
        predicates: An iterable of predicate functions to test

    Returns:
        A function that takes a value and returns True if it passes any predicate

    Examples:
        >>> is_empty = lambda x: len(x) == 0
        >>> is_short = lambda x: len(x) < 3
        >>> check = any_pass([is_empty, is_short])
        >>> check("")
        True
        >>> check("hi")
        True
        >>> check("hello")
        False
    """

    def checker(value: Any) -> bool:
        for predicate in predicates:
            if predicate(value):
                return True
        return False

    return checker
