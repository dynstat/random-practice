import asyncio
from asyncio import Future


# add a task to the event loop
async def add_task(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    await task
    return task


# run a task in the event loop
async def run_task(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    await task
    return task


# run a task in the event loop and wait for it to complete
async def run_task_and_wait(loop, coro):
    task = asyncio.ensure_future(coro, loop=loop)
    await task
    return task


# run a task in the event loop and wait for it to complete
async def run_task_and_wait_with_timeout(loop, coro, timeout):
    task = asyncio.wait_for(coro, timeout, loop=loop)
    return task


# run a task in the event loop and wait for it to complete
async def run_task_and_wait_with_timeout_and_cancel(loop, coro, timeout):
    task = asyncio.wait_for(coro, timeout, loop=loop)
    task.cancel()
    return task


# run a task in the event loop and wait for it to complete
async def run_task_and_wait_with_timeout_and_cancel_and_result(loop, coro, timeout):
    task = asyncio.wait_for(coro, timeout, loop=loop)
    task.cancel()
    return task.result()


async def main():
    my_future = Future()
    print(my_future.done())  # False

    my_future.set_result("Bright")

    print(my_future.done())  # True

    print(my_future.result())  # "Bright"

    await asyncio.sleep(1)
    print(my_future.done())  # False

    my_future.set_result("very bright")
    await asyncio.sleep(1)
    print(my_future.done())  # True

    print(my_future.result())  # "very bright"


asyncio.run(main())
