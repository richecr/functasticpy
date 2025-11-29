from typing import Any, Callable, TypeVar

T = TypeVar("T")


def assert_type(predicate: Callable[[T], bool]) -> Callable[[T], Any]:
    """Assert that a value matches a type predicate and narrow its type.

    Takes a type guard function and returns a function that either returns
    the value with narrowed type or raises an AssertionError if the predicate
    fails. This is useful for runtime type validation with compile-time type
    narrowing.

    Args:
        predicate: A type guard function that checks if a value is of type U

    Returns:
        A function that takes a value of type T and returns it as type U,
        raising AssertionError if the predicate fails

    Raises:
        AssertionError: If the value does not satisfy the predicate

    Examples:
        >>> def is_str(x: object) -> bool:
        ...     return isinstance(x, str)
        >>> assert_str = assert_type(is_str)
        >>> result = assert_str("hello")  # Returns "hello" as str
        >>> assert_str(42)  # Raises AssertionError
        Traceback (most recent call last):
        ...
        AssertionError: Type assertion failed

        >>> def is_positive(x: int) -> bool:
        ...     return x > 0
        >>> assert_positive = assert_type(is_positive)
        >>> assert_positive(5)  # Returns 5
        5
    """

    def asserter(value: T) -> Any:
        if not predicate(value):
            raise AssertionError("Type assertion failed")
        return value  # type: ignore

    return asserter
