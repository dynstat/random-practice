import asyncio


async def my_coroutine(name):

    print(f"start {name}")
    await asyncio.sleep(1)
    print(f"middle {name}")
    await asyncio.sleep(1)
    print(f"end {name}")


async def main():
    cr_list = []
    for _ in range(100):
        cr_list.append(my_coroutine("kanchan"))
        cr_list.append(my_coroutine("Vivek"))
        cr_list.append(my_coroutine("XS"))

    await asyncio.gather(*cr_list)


asyncio.run(main())
