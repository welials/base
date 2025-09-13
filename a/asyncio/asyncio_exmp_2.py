# Coroutines
"""
Source code: https://github.com/python/cpython/blob/3.13/Lib/asyncio/coroutines.py

Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.
For example, the following snippet of code prints “hello”, waits 1 second, and then prints “world”:
"""
import asyncio
import time

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
# hello
# world

"""
Note that simply calling a coroutine will not schedule it to be executed:
"""
print(main())
"""
<coroutine object main at 0x000001CABC2B65C0>
"""

"""
To actually run a coroutine, asyncio provides the following mechanisms:

The asyncio.run() function to run the top-level entry point “main()” function (see the above example.)

Awaiting on a coroutine. 
The following snippet of code will print “hello” after waiting for 1 second, 
and then print “world” after waiting for another 2 seconds:
"""

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
"""
started at 23:27:10
hello
world
finished at 23:27:13
"""

"""
The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
Let’s modify the above example and run two say_after coroutines concurrently:
"""
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
"""
started at 23:27:48
hello
world
finished at 23:27:50
"""

"""
The asyncio.TaskGroup class provides a more modern alternative to create_task(). 
Using this API, the last example becomes:
"""
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(5, 'hello'))

        task2 = tg.create_task(
            say_after(5, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
"""
started at 23:29:22
hello
world
finished at 23:29:27
"""