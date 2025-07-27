from typing import Callable, Generator, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


# Função Lazy: cada operação não será realizada até que o valor final seja consumido.
def pipe(
    value: T, *functions: Callable[[T], Union[T, Generator[U, None, None]]]
) -> Union[T, Generator[U, None, None]]:
    """
    Lazy version of pipe that processes the value through each function lazily.
    The result is calculated only when the value is consumed.
    """
    result = value  # Inicializa o resultado com o valor inicial

    # Retorna um gerador que só será consumido quando necessário
    def lazy_pipe(value: T) -> Generator[U, None, None]:
        for func in functions:
            result = func(value)  # Aplica a função

            # Se a função retornar um gerador, usamos 'yield from' para consumir lazily
            if isinstance(result, Generator):
                yield from result
            else:
                yield result

    # Retorna o gerador quando o pipeline for "lazy"
    return lazy_pipe(value)


# Funções de exemplo
def multiply_by_two(x: int) -> Generator[int, None, None]:
    """Função que gera um valor multiplicado por dois"""
    yield x * 2


def add_five(x: int) -> int:
    """Função que adiciona 5 ao valor"""
    return x + 5


# Usando o pipe com funções preguiçosas e regulares
lazy_result = pipe(3, multiply_by_two, add_five)

# Como o pipe é lazy, precisamos iterar sobre ele para obter os resultados
for result in lazy_result:
    print(result)  # Imprime 6 (3*2) e depois 11 (6+5)
