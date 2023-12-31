import asyncio
import random


async def counter(name: str):
    for i in range(0, 10):
        print(f"{name}: {i!s}")
        await asyncio.sleep(random.randint(0, 4))


async def main():
    tasks = []
    for n in range(0, 4):
        tasks.append(asyncio.create_task(counter(f"task{n}")))

    while True:
        tasks = [t for t in tasks if not t.done()]
        if len(tasks) == 0:
            return

        # await tasks[0]  # WORKS
        # asyncio.gather(*tasks)  # NOT CORRECT way to start all tasks
        await asyncio.gather(*tasks)


asyncio.run(main())
