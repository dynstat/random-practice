import asyncio
import threading
from time import sleep


def delayed_print(any_text):
    sleep(4)
    print(any_text)


# This function, when called, returns a coroutine object.
# But the body of the function doesn't get executed. (needs to be awaited to run)
async def a_delayed_print(any_text, id):
    print(f"id = {id}")
    await asyncio.sleep(4)
    print(any_text)
    return id


# a_delayed_print("1")

l = []


async def main():
    global l
    c1 = a_delayed_print("c1", 1)
    c2 = a_delayed_print("c2", 2)
    c3 = a_delayed_print("c3", 3)

    t1 = asyncio.create_task(a_delayed_print("t1", 1), name="c1")
    t2 = asyncio.create_task(a_delayed_print("t2", 2), name="c2")
    t3 = asyncio.create_task(a_delayed_print("t3", 3), name="c3")

    l = await asyncio.gather(c1, c2, c3, t1, t2, t3)
    print(l)


if __name__ == "__main__":
    # t1 = threading.Thread(target=delayed_print, args=("1",), name="t1")
    # t2 = threading.Thread(target=delayed_print, args=("2",), name="t2")
    # t3 = threading.Thread(target=delayed_print, args=("3",), name="t3")

    # t1.start()
    # t2.start()
    # t3.start()
    # ##############################
    asyncio.run(main())
