from __future__ import annotations

from typing import Mapping


def prop(key):
    """Get a property value from a mapping object (curried version).

    Returns a function that retrieves a value from a mapping (dict-like) object.
    The returned function returns None if the key doesn't exist or if the object
    is None. Raises TypeError if the object is not a Mapping.

    Args:
        key: The key to retrieve from the mapping

    Returns:
        A function that takes a mapping and returns the value for the key,
        or None if the key doesn't exist or the object is None

    Raises:
        TypeError: If the target object is not a Mapping or None

    Examples:
        >>> get_name = prop('name')
        >>> get_name({'name': 'Alice', 'age': 30})
        'Alice'
        >>> get_name({'age': 30})
        None
        >>> get_name(None)
        None
    """

    def getter(target):
        if target is None:
            return None
        if not isinstance(target, Mapping):
            raise TypeError(f"prop expected a Mapping or None, got {type(target)!r}")
        return target.get(key)

    return getter
