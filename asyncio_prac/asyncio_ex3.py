import time

# Define a coroutine function
async def my_coroutine():
    print("Coroutine started")
    time.sleep(1)  # Suspend execution for 1 second
    print("Coroutine resumed")
    time.sleep(2)  # Suspend execution for 2 seconds
    print("Coroutine ended")

# Define a simple function to run a coroutine
def run_coroutine(coro):
    try:
        coro.send(None)
    except StopIteration:
        pass

# Run the coroutine
coro = my_coroutine()
run_coroutine(coro)

# Do some other work while the coroutine is running
print("Main thread sleeping...")
time.sleep(3)
print("Main thread woke up")

# Resume the coroutine
run_coroutine(coro)
