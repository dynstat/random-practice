import asyncio
import time


def blocking_function():
    # This function takes a long time to run
    time.sleep(5)
    return "Finished blocking function"


async def main():
    loop = asyncio.get_event_loop()
    # Run the blocking function in a separate thread
    future = loop.run_in_executor(None, blocking_function)
    # Do other stuff while the blocking function is running
    print("Doing other stuff")
    # Wait for the blocking function to finish and get the result
    result = await future
    print(result)


# Run the main function
asyncio.run(main())
