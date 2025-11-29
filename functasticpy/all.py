# all.py
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def all(predicate: Callable[[T], bool]) -> Callable[[Sequence[T]], bool]:
    """Create a function that checks if all elements satisfy a predicate.

    Returns a curried function that takes a sequence and returns True only if
    all elements in the sequence satisfy the given predicate function.

    Args:
        predicate: A function that tests each element

    Returns:
        A function that takes a sequence and returns True if all elements
        satisfy the predicate, False otherwise

    Examples:
        >>> is_even = lambda x: x % 2 == 0
        >>> all_even = all(is_even)
        >>> all_even([2, 4, 6])
        True
        >>> all_even([2, 3, 6])
        False
        >>> all_positive = all(lambda x: x > 0)
        >>> all_positive([1, 2, 3])
        True
    """

    def checker(items: Sequence[T]) -> bool:
        for item in items:
            if not predicate(item):
                return False
        return True

    return checker
