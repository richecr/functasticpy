from typing import Callable, List, TypeVar, overload

T = TypeVar("T")

@overload
def concat(arr1: List[T], arr2: List[T]) -> List[T]:
    """
    Concatenate two lists.

    Args:
        arr1 (List[T]): The first list.
        arr2 (List[T]): The second list.

    Returns:
        List[T]: The concatenated list.
    """
    ...

@overload
def concat(arr2: List[T]) -> Callable[[List[T]], List[T]]:
    """
    Create a function that concatenates a list with another list.

    Args:
        arr2 (List[T]): The second list.

    Returns:
        Callable[[List[T]], List[T]]: A function that takes a list and returns the concatenated list.
    """
    ...
