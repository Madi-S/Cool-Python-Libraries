'''
This example demonstrates tqdm in async for loops
'''
import asyncio
from tqdm.asyncio import tqdm


async def main():
    a = 0
    async for i in tqdm(range(10000000)):
        a += i
    print(a)

if __name__ == '__main__':
    asyncio.run(main())
