# any.py
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def any(predicate: Callable[[T], bool]) -> Callable[[Sequence[T]], bool]:
    """Create a function that checks if any element satisfies a predicate.

    Returns a curried function that takes a sequence and returns True if at
    least one element in the sequence satisfies the given predicate function.

    Args:
        predicate: A function that tests each element

    Returns:
        A function that takes a sequence and returns True if at least one
        element satisfies the predicate, False otherwise

    Examples:
        >>> is_even = lambda x: x % 2 == 0
        >>> any_even = any(is_even)
        >>> any_even([1, 3, 5])
        False
        >>> any_even([1, 2, 3])
        True
        >>> any_negative = any(lambda x: x < 0)
        >>> any_negative([1, 2, -3])
        True
    """

    def checker(items: Sequence[T]) -> bool:
        for item in items:
            if predicate(item):
                return True
        return False

    return checker
