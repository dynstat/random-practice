# import asyncio
# import random


# async def counter(name: str):
#     for i in range(0, 10):
#         print(f"{name}: {i!s}")
#         await asyncio.sleep(random.randint(0, 4))


# async def main():
#     tasks = []
#     for n in range(0, 4):
#         tasks.append(asyncio.create_task(counter(f"task{n}")))

#     while True:
#         tasks = [t for t in tasks if not t.done()]
#         if len(tasks) == 0:
#             return

#         # await tasks[0]  # WORKS
#         # asyncio.gather(*tasks)  # NOT CORRECT way to start all tasks
#         await asyncio.gather(*tasks)


# asyncio.run(main())


##################################


import asyncio
import time
from concurrent.futures import ThreadPoolExecutor  # Changed from ProcessPoolExecutor

def fetch_data(param):
    print(f"Do something with {param}...", flush=True)
    time.sleep(param)
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"

async def main():
    # Run in Threads
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread 1 fully completed")
    result2 = await task2
    print("Thread 2 fully completed")

    # Run in Thread Pool (instead of Process Pool)
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:  # Changed from ProcessPoolExecutor
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Thread Pool 1 fully completed")
        result2 = await task2
        print("Thread Pool 2 fully completed")

    return [result1, result2]

# Run the async function
results = asyncio.run(main())
print(results)