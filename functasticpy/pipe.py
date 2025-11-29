def pipe(value, *funcs):
    """Pass a value through a series of functions.

    Args:
        value: The initial value to transform
        *funcs: Transformation functions to apply in sequence

    Returns:
        The transformed value after applying all functions in sequence

    Example:
        >>> pipe(5, lambda x: x * 2, lambda x: x + 1)  # Returns 11
        >>> pipe("hello", str.upper, lambda s: s + "!")  # Returns "HELLO!"
    """
    result = value
    for func in funcs:
        result = func(result)

    return result
