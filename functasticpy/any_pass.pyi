from typing import Callable, List, TypeVar, overload

T = TypeVar("T")

@overload
def any_pass(value: T, functions: List[Callable[[T], bool]]) -> bool:
    """
    Check if any function returns True for the given value.

    Args:
        value: The value to be checked.
        functions: A list of functions that take a single argument and return a boolean.
    Returns:
        bool: True if any function returns True for the value, False otherwise.
    """
    ...

@overload
def any_pass(functions: List[Callable[[T], bool]]) -> Callable[[T], bool]:
    """
    Check if any function returns True for the given value.

    Args:
        functions: A list of functions that take a single argument and return a boolean.
    Returns:
        Callable[[T], bool]: A function that takes a single argument and returns True if any function returns True for the value, False otherwise.
    """
    ...
