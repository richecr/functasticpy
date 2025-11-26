from __future__ import annotations

from typing import Callable, List, Tuple, TypeGuard, TypeVar, overload

S = TypeVar("S")  # tipo de entrada para os predicates com TypeGuard
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")

X = TypeVar("X")  # tipo de entrada para o caso genérico (sem TypeGuard)

@overload
def any_pass(
    predicates: Tuple[
        Callable[[S], TypeGuard[T1]],
        Callable[[S], TypeGuard[T2]],
    ],
) -> Callable[[S], TypeGuard[T1 | T2]]: ...
@overload
def any_pass(
    predicates: Tuple[
        Callable[[S], TypeGuard[T1]],
        Callable[[S], TypeGuard[T2]],
        Callable[[S], TypeGuard[T3]],
    ],
) -> Callable[[S], TypeGuard[T1 | T2 | T3]]: ...
@overload
def any_pass(
    predicates: Tuple[
        Callable[[S], TypeGuard[T1]],
        Callable[[S], TypeGuard[T2]],
        Callable[[S], TypeGuard[T3]],
        Callable[[S], TypeGuard[T4]],
    ],
) -> Callable[[S], TypeGuard[T1 | T2 | T3 | T4]]: ...
@overload
def any_pass(
    predicates: Tuple[
        Callable[[S], TypeGuard[T1]],
        Callable[[S], TypeGuard[T2]],
        Callable[[S], TypeGuard[T3]],
        Callable[[S], TypeGuard[T4]],
        Callable[[S], TypeGuard[T5]],
    ],
) -> Callable[[S], TypeGuard[T1 | T2 | T3 | T4 | T5]]: ...
@overload
def any_pass(
    predicates: Tuple[
        Callable[[S], TypeGuard[T1]],
        Callable[[S], TypeGuard[T2]],
        Callable[[S], TypeGuard[T3]],
        Callable[[S], TypeGuard[T4]],
        Callable[[S], TypeGuard[T5]],
        Callable[[S], TypeGuard[T6]],
    ],
) -> Callable[[S], TypeGuard[T1 | T2 | T3 | T4 | T5 | T6]]: ...

# fallback genérico - equivalente ao último overload do TS, mas só 1 arg
@overload
def any_pass(
    predicates: List[Callable[[X], bool]],
) -> Callable[[X], bool]: ...
