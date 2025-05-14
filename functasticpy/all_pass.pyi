from typing import Callable, List, TypeVar, overload

T = TypeVar("T")

@overload
def all_pass(value: T, functions: List[Callable[[T], bool]]) -> bool:
    """
    Check if all functions return True for the given value.

    Args:
        value: The value to be checked.
        functions: A list of functions that take a single argument and return a boolean.
    Returns:
        bool: True if all functions return True for the value, False otherwise.
    """
    ...

@overload
def all_pass(functions: List[Callable[[T], bool]]) -> Callable[[T], bool]:
    """
    Check if all functions return True for the given value.

    Args:
        functions: A list of functions that take a single argument and return a boolean.
    Returns:
        Callable[[T], bool]: A function that takes a single argument and returns True if all functions return True for the value, False otherwise.
    """
    ...
