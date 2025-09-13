import asyncio
from datetime import datetime
from asyncio import TaskGroup
#
# # Creating Tasks
# """
# asyncio.create_task(coro, *, name=None, context=None)
# Wrap the coro coroutine into a Task and schedule its execution. Return the Task object.
#
# If name is not None, it is set as the name of the task using Task.set_name().
#
# An optional keyword-only context argument allows specifying a custom contextvars.Context for the coro to run in.
# The current context copy is created when no context is provided.
#
# The task is executed in the loop returned by get_running_loop(), RuntimeError is raised if there
# is no running loop in current thread.
# Save a reference to the result of this function, to avoid a task disappearing mid-execution.
# The event loop only keeps weak references to tasks. A task that isn’t referenced elsewhere may get
# garbage collected at any time, even before it’s done.
# For reliable “fire-and-forget” background tasks, gather them in a collection:
#
# Примечание asyncio.TaskGroup.create_task()— это новая альтернатива, использующая структурный параллелизм;
# она позволяет ожидать группу связанных задач с надежными гарантиями безопасности.
# Важный Сохраните ссылку на результат этой функции, чтобы задача не исчезла во время выполнения.
# Цикл событий сохраняет только слабые ссылки на задачи. Задача, на которую нет ссылок где-либо ещё,
# может быть удалена сборщиком мусора в любой момент, даже до её завершения. Для надёжных фоновых задач,
# работающих по принципу «запустил и забыл»
#
# Exemple: # no work
#
# background_tasks = set()
#
# for i in range(10):
#     task = asyncio.create_task(some_coro(param=i))
#
#     # Add task to the set. This creates a strong reference.
#     background_tasks.add(task)
#
#     # To prevent keeping references to finished tasks forever,
#     # make each task remove its own reference from the set after
#     # completion:
#     task.add_done_callback(background_tasks.discard)
# """
# print("#1")
#
#
# background_tasks = set()
#
# async def main():
#     # using future
#     future = asyncio.get_running_loop().create_future()
#     future.add_done_callback(lambda r: print("future done callback"))
#     future.set_result("done")
#     print("future processed")
#
#     await future
#     print("future awaited (1)")
#     await future
#     print("future awaited (2)")
#
#     # using task
#     async def coroutine():
#         print("task processed")
#
#     task = asyncio.create_task(coroutine())
#     # Add task to the set. This creates a strong reference.
#     background_tasks.add(task)
#     task.add_done_callback(lambda r: print("task done callback"))
#     # To prevent keeping references to finished tasks forever,
#     # make each task remove its own reference from the set after
#     # completion:
#     task.add_done_callback(background_tasks.discard)
#     await task
#     print("task awaited (1)")
#     await task
#     print("task awaited (2)")
#
#
# asyncio.run(main())
# print(background_tasks)
# """
# Метод add_done_callback()в Python в основном используется с объектами, «подобными будущим», такими как asyncio.
# Task или concurrent.futures.Future, для регистрации вызываемого объекта (функции или метода), который будет выполнен после завершения связанной задачи или будущего.
# Цель:
# Асинхронные операции:
# В асинхронном программировании с помощью asyncioпозволяет add_done_callback()определить действия,
# которые необходимо предпринять после asyncio.Taskзавершения выполнения, независимо от того,
# было ли оно успешно завершено, вызвало исключение или было отменено.
# Пулы потоков/процессов:
# При использовании concurrent.futures.ThreadPoolExecutorили позволяет прикрепить к объекту обратный вызов ,
# который будет вызван после завершения задачи ProcessPoolExecutor, отправленной исполнителю.add_done_callback()Future
# Как это работает:
# Прикрепить обратный звонок:
# Вы вызываете add_done_callback()объект Taskor Future, передавая функцию, которую хотите выполнить, в качестве аргумента.
# Исполнение по завершении:
# Когда функция Taskили Futureпереходит в состояние «выполнено» (т. е. имеет результат, исключение или отменяется),
# вызывается зарегистрированная функция обратного вызова.
# Аргумент обратного вызова:
# Функция обратного вызова обычно получает сам Taskобъект Futureв качестве своего единственного аргумента,
# что позволяет ей проверять результат, исключение или статус отмены.
# Пример с asyncio:
# """
#
# print("#2")
# async def my_coroutine():
#     await asyncio.sleep(1)
#     return "Coroutine finished!"
#
# def callback_function(task):
#     if task.cancelled():
#         print("Task was cancelled.")
#     elif task.exception():
#         print(f"Task raised an exception: {task.exception()}")
#     else:
#         print(f"Task completed with result: {task.result()}")
#
# async def main():
#     task = asyncio.create_task(my_coroutine())
#     task.add_done_callback(callback_function)
#     await task
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
#
# print("#3")
# # Callback - context object is the actual
# # task object
# def task_cb(context):
#     print("Task completion received...")
#     print("Name of the task:%s"%context.get_name())
#     print("Wrapped coroutine object:%s"%context.get_coro())
#     print("Task is done:%s"%context.done())
#     print("Task has been cancelled:%s"%context.cancelled())
#     print("Task result:%s"%context.result())
#     print(type(context))
#     print(context)
#     print(context)
#
# # A simple Python coroutine
# async def simple_coroutine():
#     await asyncio.sleep(1)
#     return 1
#
# # Create an asyncio.Task object
# async def main():
#     t1 = asyncio.create_task(simple_coroutine())
#     t1.add_done_callback(task_cb)
#     await t1
#     print("Coroutine main() exiting")
# #
# # Execute the task
# el = asyncio.new_event_loop()
# asyncio.set_event_loop(el)
# asyncio.run(main())
#
# r"""
# Task completion received...
# Name of the task:Task-10
# Wrapped coroutine object:<coroutine object simple_coroutine at 0x000001BBD9F765C0>
# Task is done:True
# Task has been cancelled:False
# Task result:1
# <class '_asyncio.Task'>
# <Task finished name='Task-10' coro=<simple_coroutine() done, defined at E:\PycharmProjects\Base\a\asyncio\asyncio_exmp_4.py:134> result=1>
# <Task finished name='Task-10' coro=<simple_coroutine() done, defined at E:\PycharmProjects\Base\a\asyncio\asyncio_exmp_4.py:134> result=1>
# Coroutine main() exiting
# """
# #
# #
# # # Task Cancellation
# """
# Tasks can easily and safely be cancelled. When a task is cancelled, asyncio.
# CancelledError will be raised in the task at the next opportunity.
#
# It is recommended that coroutines use try/finally blocks to robustly perform clean-up logic.
# In case asyncio.CancelledError is explicitly caught, it should generally be propagated when clean-up is complete.
# asyncio.CancelledError directly subclasses BaseException so most code will not need to be aware of it.
#
# The asyncio components that enable structured concurrency, like asyncio.TaskGroup and asyncio.timeout(),
# are implemented using cancellation internally and might misbehave if a coroutine swallows asyncio.CancelledError.
# Similarly, user code should not generally call uncancel. However, in cases when suppressing asyncio.
# CancelledError is truly desired, it is necessary to also call uncancel() to completely remove the cancellation state.
# """
#
# # Task Groups
# """
# Task groups combine a task creation API with a convenient and reliable way to wait for all tasks in the group to finish.
#
# class asyncio.TaskGroup
# An asynchronous context manager holding a group of tasks.
# Tasks can be added to the group using create_task(). All tasks are awaited when the context manager exits.
#
# Added in version 3.11.
#
# create_task(coro, *, name=None, context=None)
# Create a task in this task group. The signature matches that of asyncio.create_task().
# If the task group is inactive (e.g. not yet entered, already finished, or in the process of shutting down), we will close the given coro.
# """
# # Example:
# print("#4")
# async def some_coro(param):
#     return param
# async def another_coro(param):
#     return param
#
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         task1 = tg.create_task(some_coro(...))
#         task2 = tg.create_task(another_coro(...))
#     print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")
#
# asyncio.run(main())
#
# #
# #
# # # Terminating a Task Group
# """
# While terminating a task group is not natively supported by the standard library,
# termination can be achieved by adding an exception-raising task to the task group
# and ignoring the raised exception:
# """
#
#
# print("#5")
# class TerminateTaskGroup(Exception):
#     """Exception raised to terminate a task group."""
#
# async def force_terminate_task_group():
#     """Used to force termination of a task group."""
#     raise TerminateTaskGroup()
#
# async def job(task_id, sleep_time):
#     print(f'Task {task_id}: start')
#     await asyncio.sleep(sleep_time)
#     print(f'Task {task_id}: done')
#
# async def main_2():
#     try:
#         async with TaskGroup() as group:
#             # spawn some tasks
#             group.create_task(job(1, 0.5))
#             group.create_task(job(2, 1.5))
#             # sleep for 1 second
#             await asyncio.sleep(1)
#             # add an exception-raising task to force the group to terminate
#             group.create_task(force_terminate_task_group())
#     except* TerminateTaskGroup:
#         pass
#
# asyncio.run(main_2())
# """
# Expected output:
#
# Task 1: start
# Task 2: start
# Task 1: done
# """
#
# # Sleeping
#
# """
# async asyncio.sleep(delay, result=None)
# Block for delay seconds.
#
# If result is provided, it is returned to the caller when the coroutine completes.
#
# sleep() always suspends the current task, allowing other tasks to run.
#
# Setting the delay to 0 provides an optimized path to allow other tasks to run.
# This can be used by long-running functions to avoid blocking the event loop for the full duration of the function call.
#
# Example of coroutine displaying the current date every second for 5 seconds:
#
# """
#
# print("#6")
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
# asyncio.run(display_date())
# """
# 2025-09-13 12:06:39.537412
# 2025-09-13 12:06:40.538715
# 2025-09-13 12:06:41.539435
# 2025-09-13 12:06:42.551453
# 2025-09-13 12:06:43.554653
# """
# async def main():
#     result = await asyncio.sleep(0.5, 'done')
#     print(result)
#
#
# asyncio.run(main())
# # done


# Running Tasks Concurrently
"""
awaitable asyncio.gather(*aws, return_exceptions=False)
Run awaitable objects in the aws sequence concurrently.

If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.

If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in aws.

If return_exceptions is False (default), the first raised exception is immediately propagated to the task that awaits on gather(). Other awaitables in the aws sequence won’t be cancelled and will continue to run.

If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list.

If gather() is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.

If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case. This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.

Note A new alternative to create and run tasks concurrently and wait for their completion is asyncio.TaskGroup. TaskGroup provides stronger safety guarantees than gather for scheduling a nesting of subtasks: if a task (or a subtask, a task scheduled by a task) raises an exception, TaskGroup will, while gather will not, cancel the remaining scheduled tasks).
Example:
"""
print("#7")

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]
"""
Note If return_exceptions is false, cancelling gather() after it has been marked done won’t cancel any submitted awaitables. For instance, gather can be marked done after propagating an exception to the caller, therefore, calling gather.cancel() after catching an exception (raised by one of the awaitables) from gather won’t cancel any other awaitables.
Changed in version 3.7: If the gather itself is cancelled, the cancellation is propagated regardless of return_exceptions.

Changed in version 3.10: Removed the loop parameter.

Deprecated since version 3.10: Deprecation warning is emitted if no positional arguments are provided or not all positional arguments are Future-like objects and there is no running event loop.

Eager Task Factory
asyncio.eager_task_factory(loop, coro, *, name=None, context=None)
A task factory for eager task execution.

When using this factory (via loop.set_task_factory(asyncio.eager_task_factory)), coroutines begin execution synchronously during Task construction. Tasks are only scheduled on the event loop if they block. This can be a performance improvement as the overhead of loop scheduling is avoided for coroutines that complete synchronously.

A common example where this is beneficial is coroutines which employ caching or memoization to avoid actual I/O when possible.

Note Immediate execution of the coroutine is a semantic change. If the coroutine returns or raises, the task is never scheduled to the event loop. If the coroutine execution blocks, the task is scheduled to the event loop. This change may introduce behavior changes to existing applications. For example, the application’s task execution order is likely to change.
Added in version 3.12.

asyncio.create_eager_task_factory(custom_task_constructor)
Create an eager task factory, similar to eager_task_factory(), using the provided custom_task_constructor when creating a new task instead of the default Task.

custom_task_constructor must be a callable with the signature matching the signature of Task.__init__. The callable must return a asyncio.Task-compatible object.

This function returns a callable intended to be used as a task factory of an event loop via loop.set_task_factory(factory)).

Added in version 3.12.

Shielding From Cancellation
awaitable asyncio.shield(aw)
Protect an awaitable object from being cancelled.

If aw is a coroutine it is automatically scheduled as a Task.

The statement:

task = asyncio.create_task(something())
res = await shield(task)
is equivalent to:

res = await something()
except that if the coroutine containing it is cancelled, the Task running in something() is not cancelled. From the point of view of something(), the cancellation did not happen. Although its caller is still cancelled, so the “await” expression still raises a CancelledError.

If something() is cancelled by other means (i.e. from within itself) that would also cancel shield().

If it is desired to completely ignore cancellation (not recommended) the shield() function should be combined with a try/except clause, as follows:

task = asyncio.create_task(something())
try:
    res = await shield(task)
except CancelledError:
    res = None
Important Save a reference to tasks passed to this function, to avoid a task disappearing mid-execution. The event loop only keeps weak references to tasks. A task that isn’t referenced elsewhere may get garbage collected at any time, even before it’s done.
Changed in version 3.10: Removed the loop parameter.

Deprecated since version 3.10: Deprecation warning is emitted if aw is not Future-like object and there is no running event loop.

Timeouts
asyncio.timeout(delay)
Return an asynchronous context manager that can be used to limit the amount of time spent waiting on something.

delay can either be None, or a float/int number of seconds to wait. If delay is None, no time limit will be applied; this can be useful if the delay is unknown when the context manager is created.

In either case, the context manager can be rescheduled after creation using Timeout.reschedule().

Example:

async def main():
    async with asyncio.timeout(10):
        await long_running_task()
If long_running_task takes more than 10 seconds to complete, the context manager will cancel the current task and handle the resulting asyncio.CancelledError internally, transforming it into a TimeoutError which can be caught and handled.

Note The asyncio.timeout() context manager is what transforms the asyncio.CancelledError into a TimeoutError, which means the TimeoutError can only be caught outside of the context manager.
Example of catching TimeoutError:

async def main():
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
The context manager produced by asyncio.timeout() can be rescheduled to a different deadline and inspected.

class asyncio.Timeout(when)
An asynchronous context manager for cancelling overdue coroutines.

when should be an absolute time at which the context should time out, as measured by the event loop’s clock:

If when is None, the timeout will never trigger.

If when < loop.time(), the timeout will trigger on the next iteration of the event loop.

when() → float | None
Return the current deadline, or None if the current deadline is not set.

reschedule(when: float | None)
Reschedule the timeout.

expired() → bool
Return whether the context manager has exceeded its deadline (expired).

Example:

async def main():
    try:
        # We do not know the timeout when starting, so we pass ``None``.
        async with asyncio.timeout(None) as cm:
            # We know the timeout now, so we reschedule it.
            new_deadline = get_running_loop().time() + 10
            cm.reschedule(new_deadline)

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired():
        print("Looks like we haven't finished on time.")
Timeout context managers can be safely nested.

Added in version 3.11.

asyncio.timeout_at(when)
Similar to asyncio.timeout(), except when is the absolute time to stop waiting, or None.

Example:

async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    try:
        async with asyncio.timeout_at(deadline):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
Added in version 3.11.

async asyncio.wait_for(aw, timeout)
Wait for the aw awaitable to complete with a timeout.

If aw is a coroutine it is automatically scheduled as a Task.

timeout can either be None or a float or int number of seconds to wait for. If timeout is None, block until the future completes.

If a timeout occurs, it cancels the task and raises TimeoutError.

To avoid the task cancellation, wrap it in shield().

The function will wait until the future is actually cancelled, so the total wait time may exceed the timeout. If an exception happens during cancellation, it is propagated.

If the wait is cancelled, the future aw is also cancelled.

Example:

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
Changed in version 3.7: When aw is cancelled due to a timeout, wait_for waits for aw to be cancelled. Previously, it raised TimeoutError immediately.

Changed in version 3.10: Removed the loop parameter.

Changed in version 3.11: Raises TimeoutError instead of asyncio.TimeoutError.

Waiting Primitives
async asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)
Run Future and Task instances in the aws iterable concurrently and block until the condition specified by return_when.

The aws iterable must not be empty.

Returns two sets of Tasks/Futures: (done, pending).

Usage:

done, pending = await asyncio.wait(aws)
timeout (a float or int), if specified, can be used to control the maximum number of seconds to wait before returning.

Note that this function does not raise TimeoutError. Futures or Tasks that aren’t done when the timeout occurs are simply returned in the second set.

return_when indicates when this function should return. It must be one of the following constants:

Constant

Description

asyncio.FIRST_COMPLETED
The function will return when any future finishes or is cancelled.

asyncio.FIRST_EXCEPTION
The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.

asyncio.ALL_COMPLETED
The function will return when all futures finish or are cancelled.

Unlike wait_for(), wait() does not cancel the futures when a timeout occurs.

Changed in version 3.10: Removed the loop parameter.

Changed in version 3.11: Passing coroutine objects to wait() directly is forbidden.

Changed in version 3.12: Added support for generators yielding tasks.

asyncio.as_completed(aws, *, timeout=None)
Run awaitable objects in the aws iterable concurrently. The returned object can be iterated to obtain the results of the awaitables as they finish.

The object returned by as_completed() can be iterated as an asynchronous iterator or a plain iterator. When asynchronous iteration is used, the originally-supplied awaitables are yielded if they are tasks or futures. This makes it easy to correlate previously-scheduled tasks with their results. Example:

ipv4_connect = create_task(open_connection("127.0.0.1", 80))
ipv6_connect = create_task(open_connection("::1", 80))
tasks = [ipv4_connect, ipv6_connect]

async for earliest_connect in as_completed(tasks):
    # earliest_connect is done. The result can be obtained by
    # awaiting it or calling earliest_connect.result()
    reader, writer = await earliest_connect

    if earliest_connect is ipv6_connect:
        print("IPv6 connection established.")
    else:
        print("IPv4 connection established.")
During asynchronous iteration, implicitly-created tasks will be yielded for supplied awaitables that aren’t tasks or futures.

When used as a plain iterator, each iteration yields a new coroutine that returns the result or raises the exception of the next completed awaitable. This pattern is compatible with Python versions older than 3.13:

ipv4_connect = create_task(open_connection("127.0.0.1", 80))
ipv6_connect = create_task(open_connection("::1", 80))
tasks = [ipv4_connect, ipv6_connect]

for next_connect in as_completed(tasks):
    # next_connect is not one of the original task objects. It must be
    # awaited to obtain the result value or raise the exception of the
    # awaitable that finishes next.
    reader, writer = await next_connect
A TimeoutError is raised if the timeout occurs before all awaitables are done. This is raised by the async for loop during asynchronous iteration or by the coroutines yielded during plain iteration.

Changed in version 3.10: Removed the loop parameter.

Deprecated since version 3.10: Deprecation warning is emitted if not all awaitable objects in the aws iterable are Future-like objects and there is no running event loop.

Changed in version 3.12: Added support for generators yielding tasks.

Changed in version 3.13: The result can now be used as either an asynchronous iterator or as a plain iterator (previously it was only a plain iterator).

Running in Threads
async asyncio.to_thread(func, /, *args, **kwargs)
Asynchronously run function func in a separate thread.

Any *args and **kwargs supplied for this function are directly passed to func. Also, the current contextvars.Context is propagated, allowing context variables from the event loop thread to be accessed in the separate thread.

Return a coroutine that can be awaited to get the eventual result of func.

This coroutine function is primarily intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were run in the main thread. For example:

def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54
Directly calling blocking_io() in any coroutine would block the event loop for its duration, resulting in an additional 1 second of run time. Instead, by using asyncio.to_thread(), we can run it in a separate thread without blocking the event loop.

Note Due to the GIL, asyncio.to_thread() can typically only be used to make IO-bound functions non-blocking. However, for extension modules that release the GIL or alternative Python implementations that don’t have one, asyncio.to_thread() can also be used for CPU-bound functions.
Added in version 3.9.

Scheduling From Other Threads
asyncio.run_coroutine_threadsafe(coro, loop)
Submit a coroutine to the given event loop. Thread-safe.

Return a concurrent.futures.Future to wait for the result from another OS thread.

This function is meant to be called from a different OS thread than the one where the event loop is running. Example:

# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
If an exception is raised in the coroutine, the returned Future will be notified. It can also be used to cancel the task in the event loop:

try:
    result = future.result(timeout)
except TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')
See the concurrency and multithreading section of the documentation.

Unlike other asyncio functions this function requires the loop argument to be passed explicitly.

Added in version 3.5.1.

Introspection
asyncio.current_task(loop=None)
Return the currently running Task instance, or None if no task is running.

If loop is None get_running_loop() is used to get the current loop.

Added in version 3.7.

asyncio.all_tasks(loop=None)
Return a set of not yet finished Task objects run by the loop.

If loop is None, get_running_loop() is used for getting current loop.

Added in version 3.7.

asyncio.iscoroutine(obj)
Return True if obj is a coroutine object.

Added in version 3.4.

Task Object
class asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)
A Future-like object that runs a Python coroutine. Not thread-safe.

Tasks are used to run coroutines in event loops. If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future. When the Future is done, the execution of the wrapped coroutine resumes.

Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations.

Use the high-level asyncio.create_task() function to create Tasks, or the low-level loop.create_task() or ensure_future() functions. Manual instantiation of Tasks is discouraged.

To cancel a running Task use the cancel() method. Calling it will cause the Task to throw a CancelledError exception into the wrapped coroutine. If a coroutine is awaiting on a Future object during cancellation, the Future object will be cancelled.

cancelled() can be used to check if the Task was cancelled. The method returns True if the wrapped coroutine did not suppress the CancelledError exception and was actually cancelled.

asyncio.Task inherits from Future all of its APIs except Future.set_result() and Future.set_exception().

An optional keyword-only context argument allows specifying a custom contextvars.Context for the coro to run in. If no context is provided, the Task copies the current context and later runs its coroutine in the copied context.

An optional keyword-only eager_start argument allows eagerly starting the execution of the asyncio.Task at task creation time. If set to True and the event loop is running, the task will start executing the coroutine immediately, until the first time the coroutine blocks. If the coroutine returns or raises without blocking, the task will be finished eagerly and will skip scheduling to the event loop.

Changed in version 3.7: Added support for the contextvars module.

Changed in version 3.8: Added the name parameter.

Deprecated since version 3.10: Deprecation warning is emitted if loop is not specified and there is no running event loop.

Changed in version 3.11: Added the context parameter.

Changed in version 3.12: Added the eager_start parameter.

done()
Return True if the Task is done.

A Task is done when the wrapped coroutine either returned a value, raised an exception, or the Task was cancelled.

result()
Return the result of the Task.

If the Task is done, the result of the wrapped coroutine is returned (or if the coroutine raised an exception, that exception is re-raised.)

If the Task has been cancelled, this method raises a CancelledError exception.

If the Task’s result isn’t yet available, this method raises an InvalidStateError exception.

exception()
Return the exception of the Task.

If the wrapped coroutine raised an exception that exception is returned. If the wrapped coroutine returned normally this method returns None.

If the Task has been cancelled, this method raises a CancelledError exception.

If the Task isn’t done yet, this method raises an InvalidStateError exception.

add_done_callback(callback, *, context=None)
Add a callback to be run when the Task is done.

This method should only be used in low-level callback-based code.

See the documentation of Future.add_done_callback() for more details.

remove_done_callback(callback)
Remove callback from the callbacks list.

This method should only be used in low-level callback-based code.

See the documentation of Future.remove_done_callback() for more details.

get_stack(*, limit=None)
Return the list of stack frames for this Task.

If the wrapped coroutine is not done, this returns the stack where it is suspended. If the coroutine has completed successfully or was cancelled, this returns an empty list. If the coroutine was terminated by an exception, this returns the list of traceback frames.

The frames are always ordered from oldest to newest.

Only one stack frame is returned for a suspended coroutine.

The optional limit argument sets the maximum number of frames to return; by default all available frames are returned. The ordering of the returned list differs depending on whether a stack or a traceback is returned: the newest frames of a stack are returned, but the oldest frames of a traceback are returned. (This matches the behavior of the traceback module.)

print_stack(*, limit=None, file=None)
Print the stack or traceback for this Task.

This produces output similar to that of the traceback module for the frames retrieved by get_stack().

The limit argument is passed to get_stack() directly.

The file argument is an I/O stream to which the output is written; by default output is written to sys.stdout.

get_coro()
Return the coroutine object wrapped by the Task.

Note This will return None for Tasks which have already completed eagerly. See the Eager Task Factory.
Added in version 3.8.

Changed in version 3.12: Newly added eager task execution means result may be None.

get_context()
Return the contextvars.Context object associated with the task.

Added in version 3.12.

get_name()
Return the name of the Task.

If no name has been explicitly assigned to the Task, the default asyncio Task implementation generates a default name during instantiation.

Added in version 3.8.

set_name(value)
Set the name of the Task.

The value argument can be any object, which is then converted to a string.

In the default Task implementation, the name will be visible in the repr() output of a task object.

Added in version 3.8.

cancel(msg=None)
Request the Task to be cancelled.

If the Task is already done or cancelled, return False, otherwise, return True.

The method arranges for a CancelledError exception to be thrown into the wrapped coroutine on the next cycle of the event loop.

The coroutine then has a chance to clean up or even deny the request by suppressing the exception with a try … … except CancelledError … finally block. Therefore, unlike Future.cancel(), Task.cancel() does not guarantee that the Task will be cancelled, although suppressing cancellation completely is not common and is actively discouraged. Should the coroutine nevertheless decide to suppress the cancellation, it needs to call Task.uncancel() in addition to catching the exception.

Changed in version 3.9: Added the msg parameter.

Changed in version 3.11: The msg parameter is propagated from cancelled task to its awaiter.

The following example illustrates how coroutines can intercept the cancellation request:

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
cancelled()
Return True if the Task is cancelled.

The Task is cancelled when the cancellation was requested with cancel() and the wrapped coroutine propagated the CancelledError exception thrown into it.

uncancel()
Decrement the count of cancellation requests to this Task.

Returns the remaining number of cancellation requests.

Note that once execution of a cancelled task completed, further calls to uncancel() are ineffective.

Added in version 3.11.

This method is used by asyncio’s internals and isn’t expected to be used by end-user code. In particular, if a Task gets successfully uncancelled, this allows for elements of structured concurrency like Task Groups and asyncio.timeout() to continue running, isolating cancellation to the respective structured block. For example:

async def make_request_with_timeout():
    try:
        async with asyncio.timeout(1):
            # Structured block affected by the timeout:
            await make_request()
            await make_another_request()
    except TimeoutError:
        log("There was a timeout")
    # Outer code not affected by the timeout:
    await unrelated_code()
While the block with make_request() and make_another_request() might get cancelled due to the timeout, unrelated_code() should continue running even in case of the timeout. This is implemented with uncancel(). TaskGroup context managers use uncancel() in a similar fashion.

If end-user code is, for some reason, suppressing cancellation by catching CancelledError, it needs to call this method to remove the cancellation state.

When this method decrements the cancellation count to zero, the method checks if a previous cancel() call had arranged for CancelledError to be thrown into the task. If it hasn’t been thrown yet, that arrangement will be rescinded (by resetting the internal _must_cancel flag).

Changed in version 3.13: Changed to rescind pending cancellation requests upon reaching zero.

cancelling()
Return the number of pending cancellation requests to this Task, i.e., the number of calls to cancel() less the number of uncancel() calls.

Note that if this number is greater than zero but the Task is still executing, cancelled() will still return False. This is because this number can be lowered by calling uncancel(), which can lead to the task not being cancelled after all if the cancellation requests go down to zero.

This method is used by asyncio’s internals and isn’t expected to be used by end-user code. See uncancel() for more details.
"""