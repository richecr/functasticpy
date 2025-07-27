from typing import Callable, Generator, List, TypeVar, overload

T = TypeVar("T")

@overload
def difference(arr1: List[T], arr2: List[T]) -> List[T]:
    """
    Calculate the difference between two lists.

    Args:
        arr1 (List[T]): The first list.
        arr2 (List[T]): The second list.

    Returns:
        List[T]: A list containing elements from arr1 that are not in arr2.
    """
    ...

@overload
def difference(arr2: List[T]) -> Callable[[List[T]], Generator[T, None, None]]:
    """
    Create a curried function to calculate the difference with a second list.

    Args:
        arr2 (List[T]): The second list.

    Returns:
        Callable[[List[T]], List[T]]: A function that takes the first list and returns the difference.
    """
    ...
