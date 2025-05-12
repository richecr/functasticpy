import asyncio
from typing import List

from functasticpy.pipe import pipe


async def sum_1_async(x: List[int]) -> List[int]:
    await asyncio.sleep(1)
    return [i + 1 for i in x]


async def multiple_2_async(x: List[int]) -> List[str]:
    await asyncio.sleep(1)
    return ["a" * i for i in x]


async def main():
    a = await pipe(
        [1, 2, 3],
        sum_1_async,
        multiple_2_async,
    )
    print(a)


# Rodando a função main
asyncio.run(main())
