from __future__ import annotations

from typing import Callable, TypeVar, overload

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")
G = TypeVar("G")
H = TypeVar("H")

@overload
def pipe(value: A, op1: Callable[[A], B]) -> B: ...
@overload
def pipe(value: A, op1: Callable[[A], B], op2: Callable[[B], C]) -> C: ...
@overload
def pipe(
    value: A,
    op1: Callable[[A], B],
    op2: Callable[[B], C],
    op3: Callable[[C], D],
) -> D: ...
@overload
def pipe(
    value: A,
    op1: Callable[[A], B],
    op2: Callable[[B], C],
    op3: Callable[[C], D],
    op4: Callable[[D], E],
) -> E: ...
@overload
def pipe(
    value: A,
    op1: Callable[[A], B],
    op2: Callable[[B], C],
    op3: Callable[[C], D],
    op4: Callable[[D], E],
    op5: Callable[[E], F],
) -> F: ...
@overload
def pipe(
    value: A,
    op1: Callable[[A], B],
    op2: Callable[[B], C],
    op3: Callable[[C], D],
    op4: Callable[[D], E],
    op5: Callable[[E], F],
    op6: Callable[[F], G],
) -> G: ...
@overload
def pipe(
    value: A,
    op1: Callable[[A], B],
    op2: Callable[[B], C],
    op3: Callable[[C], D],
    op4: Callable[[D], E],
    op5: Callable[[E], F],
    op6: Callable[[F], G],
    op7: Callable[[G], H],
) -> H: ...
