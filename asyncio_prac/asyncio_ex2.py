import asyncio


async def greet(name):
    print("Hello,", name)
    await asyncio.sleep(1)
    print("Nice to meet you,", name)


# Using the coroutine
async def main():
    await greet("Alice")
    await greet("Bob")


asyncio.run(main())
