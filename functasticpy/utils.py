from typing import Any


def is_hashable(obj: Any) -> bool:
    try:
        obj.__hash__()
        return True
    except TypeError:
        return False
