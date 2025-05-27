from typing import Callable, Dict, List, TypeVar, overload

T = TypeVar("T")
U = TypeVar("U")

@overload
def count_by(arr: List[T], fn: Callable[[T], U]) -> Dict[U, int]:
    """
    Count occurrences of elements in a list based on a function.

    Args:
        arr (List[T]): The list to count elements from.
        fn (Callable[[T], U]): The function to apply to each element.

    Returns:
        Dict[U, int]: A dictionary with keys as the result of the function and values as counts.
    """
    ...

@overload
def count_by(fn: Callable[[T], U]) -> Callable[[List[T]], Dict[U, int]]:
    """
    Create a curried version of count_by.

    Args:
        fn (Callable[[T], U]): The function to apply to each element.

    Returns:
        Callable[[List[T]], Dict[U, int]]: A function that takes a list and returns a count dictionary.
    """
    ...
