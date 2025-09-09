import asyncio

# Awaitables
"""
We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects: coroutines, Tasks, and Futures.
Coroutines
Python coroutines are awaitables and therefore can be awaited from other coroutines:
"""

async def nested():
    return 42

async def nested_2():
    return 24

# ERROR
#
# async def main():
#         # Nothing happens if we just call "nested()".
#         # A coroutine object is created but not awaited,
#         # so it *won't run at all*.
#         nested()  # will raise a "RuntimeWarning".
# asyncio.run(main())
print("#1")
async def main_1():
    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main_1())


# Tasks
"""
Tasks are used to schedule coroutines concurrently.

When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:
"""



async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)
print("#2")
asyncio.run(main())


# Futures
"""
A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.

When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.

Future objects in asyncio are needed to allow callback-based code to be used with async/await.

Normally there is no need to create Future objects at the application level code.

Future objects, sometimes exposed by libraries and some asyncio APIs, can be awaited:
"""

async def main():
    print(await nested())

    # this is also valid:
    res = await asyncio.gather(
        nested(),
        nested_2()
    )
    print(res)

print("#3")
asyncio.run(main())
"""
A good example of a low-level function that returns a Future object is loop.run_in_executor().
"""