import asyncio
import random


async def get_some_values_from_io():
    # Some IO code which returns a list of values
    await asyncio.sleep(random.randint(0, 3))
    rand_list = [random.randint(1, 20) for _ in range(5)]
    print("values list returned")
    return rand_list


vals = []


async def fetcher():
    while True:
        io_vals = await get_some_values_from_io()

        for val in io_vals:
            vals.append(val)
        print("fetcher DONE")


async def monitor():
    while True:
        print("looking..")
        print(len(vals))

        await asyncio.sleep(0.5)
        print("printing list status")


async def main():
    t1 = asyncio.create_task(fetcher())
    t2 = asyncio.create_task(monitor())
    await asyncio.gather(t1, t2)


asyncio.run(main())
