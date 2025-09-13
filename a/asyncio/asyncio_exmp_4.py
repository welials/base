import asyncio
from datetime import datetime
from asyncio import TaskGroup

# Creating Tasks
"""
asyncio.create_task(coro, *, name=None, context=None)
Wrap the coro coroutine into a Task and schedule its execution. Return the Task object.

If name is not None, it is set as the name of the task using Task.set_name().

An optional keyword-only context argument allows specifying a custom contextvars.Context for the coro to run in. 
The current context copy is created when no context is provided.

The task is executed in the loop returned by get_running_loop(), RuntimeError is raised if there 
is no running loop in current thread.
Save a reference to the result of this function, to avoid a task disappearing mid-execution. 
The event loop only keeps weak references to tasks. A task that isn’t referenced elsewhere may get 
garbage collected at any time, even before it’s done. 
For reliable “fire-and-forget” background tasks, gather them in a collection:

Примечание asyncio.TaskGroup.create_task()— это новая альтернатива, использующая структурный параллелизм; 
она позволяет ожидать группу связанных задач с надежными гарантиями безопасности.
Важный Сохраните ссылку на результат этой функции, чтобы задача не исчезла во время выполнения. 
Цикл событий сохраняет только слабые ссылки на задачи. Задача, на которую нет ссылок где-либо ещё, 
может быть удалена сборщиком мусора в любой момент, даже до её завершения. Для надёжных фоновых задач, 
работающих по принципу «запустил и забыл»

Exemple: # no work

background_tasks = set()

for i in range(10):
    task = asyncio.create_task(some_coro(param=i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
"""
print("#1")


background_tasks = set()

async def main():
    # using future
    future = asyncio.get_running_loop().create_future()
    future.add_done_callback(lambda r: print("future done callback"))
    future.set_result("done")
    print("future processed")

    await future
    print("future awaited (1)")
    await future
    print("future awaited (2)")

    # using task
    async def coroutine():
        print("task processed")

    task = asyncio.create_task(coroutine())
    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)
    task.add_done_callback(lambda r: print("task done callback"))
    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
    await task
    print("task awaited (1)")
    await task
    print("task awaited (2)")


asyncio.run(main())
print(background_tasks)
"""
Метод add_done_callback()в Python в основном используется с объектами, «подобными будущим», такими как asyncio.
Task или concurrent.futures.Future, для регистрации вызываемого объекта (функции или метода), который будет выполнен после завершения связанной задачи или будущего.
Цель:
Асинхронные операции:
В асинхронном программировании с помощью asyncioпозволяет add_done_callback()определить действия, 
которые необходимо предпринять после asyncio.Taskзавершения выполнения, независимо от того, 
было ли оно успешно завершено, вызвало исключение или было отменено.
Пулы потоков/процессов:
При использовании concurrent.futures.ThreadPoolExecutorили позволяет прикрепить к объекту обратный вызов , 
который будет вызван после завершения задачи ProcessPoolExecutor, отправленной исполнителю.add_done_callback()Future
Как это работает:
Прикрепить обратный звонок:
Вы вызываете add_done_callback()объект Taskor Future, передавая функцию, которую хотите выполнить, в качестве аргумента.
Исполнение по завершении:
Когда функция Taskили Futureпереходит в состояние «выполнено» (т. е. имеет результат, исключение или отменяется), 
вызывается зарегистрированная функция обратного вызова.
Аргумент обратного вызова:
Функция обратного вызова обычно получает сам Taskобъект Futureв качестве своего единственного аргумента, 
что позволяет ей проверять результат, исключение или статус отмены.
Пример с asyncio:
"""

print("#2")
async def my_coroutine():
    await asyncio.sleep(1)
    return "Coroutine finished!"

def callback_function(task):
    if task.cancelled():
        print("Task was cancelled.")
    elif task.exception():
        print(f"Task raised an exception: {task.exception()}")
    else:
        print(f"Task completed with result: {task.result()}")

async def main():
    task = asyncio.create_task(my_coroutine())
    task.add_done_callback(callback_function)
    await task

if __name__ == "__main__":
    asyncio.run(main())


print("#3")
# Callback - context object is the actual
# task object
def task_cb(context):
    print("Task completion received...")
    print("Name of the task:%s"%context.get_name())
    print("Wrapped coroutine object:%s"%context.get_coro())
    print("Task is done:%s"%context.done())
    print("Task has been cancelled:%s"%context.cancelled())
    print("Task result:%s"%context.result())
    print(type(context))
    print(context)
    print(context)

# A simple Python coroutine
async def simple_coroutine():
    await asyncio.sleep(1)
    return 1

# Create an asyncio.Task object
async def main():
    t1 = asyncio.create_task(simple_coroutine())
    t1.add_done_callback(task_cb)
    await t1
    print("Coroutine main() exiting")
#
# Execute the task
el = asyncio.new_event_loop()
asyncio.set_event_loop(el)
asyncio.run(main())

r"""
Task completion received...
Name of the task:Task-10
Wrapped coroutine object:<coroutine object simple_coroutine at 0x000001BBD9F765C0>
Task is done:True
Task has been cancelled:False
Task result:1
<class '_asyncio.Task'>
<Task finished name='Task-10' coro=<simple_coroutine() done, defined at E:\PycharmProjects\Base\a\asyncio\asyncio_exmp_4.py:134> result=1>
<Task finished name='Task-10' coro=<simple_coroutine() done, defined at E:\PycharmProjects\Base\a\asyncio\asyncio_exmp_4.py:134> result=1>
Coroutine main() exiting
"""
#
#
# # Task Cancellation
"""
Tasks can easily and safely be cancelled. When a task is cancelled, asyncio.
CancelledError will be raised in the task at the next opportunity.

It is recommended that coroutines use try/finally blocks to robustly perform clean-up logic. 
In case asyncio.CancelledError is explicitly caught, it should generally be propagated when clean-up is complete. 
asyncio.CancelledError directly subclasses BaseException so most code will not need to be aware of it.

The asyncio components that enable structured concurrency, like asyncio.TaskGroup and asyncio.timeout(), 
are implemented using cancellation internally and might misbehave if a coroutine swallows asyncio.CancelledError. 
Similarly, user code should not generally call uncancel. However, in cases when suppressing asyncio.
CancelledError is truly desired, it is necessary to also call uncancel() to completely remove the cancellation state.
"""

# Task Groups
"""
Task groups combine a task creation API with a convenient and reliable way to wait for all tasks in the group to finish.

class asyncio.TaskGroup
An asynchronous context manager holding a group of tasks. 
Tasks can be added to the group using create_task(). All tasks are awaited when the context manager exits.

Added in version 3.11.

create_task(coro, *, name=None, context=None)
Create a task in this task group. The signature matches that of asyncio.create_task(). 
If the task group is inactive (e.g. not yet entered, already finished, or in the process of shutting down), we will close the given coro.
"""
# Example:
print("#4")
async def some_coro(param):
    return param
async def another_coro(param):
    return param

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

asyncio.run(main())

#
#
# # Terminating a Task Group
"""
While terminating a task group is not natively supported by the standard library, 
termination can be achieved by adding an exception-raising task to the task group 
and ignoring the raised exception:
"""


print("#5")
class TerminateTaskGroup(Exception):
    """Exception raised to terminate a task group."""

async def force_terminate_task_group():
    """Used to force termination of a task group."""
    raise TerminateTaskGroup()

async def job(task_id, sleep_time):
    print(f'Task {task_id}: start')
    await asyncio.sleep(sleep_time)
    print(f'Task {task_id}: done')

async def main_2():
    try:
        async with TaskGroup() as group:
            # spawn some tasks
            group.create_task(job(1, 0.5))
            group.create_task(job(2, 1.5))
            # sleep for 1 second
            await asyncio.sleep(1)
            # add an exception-raising task to force the group to terminate
            group.create_task(force_terminate_task_group())
    except* TerminateTaskGroup:
        pass

asyncio.run(main_2())
"""
Expected output:

Task 1: start
Task 2: start
Task 1: done
"""


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
# Setting the delay to 0 provides an optimized path to allow other tasks to run. This can be used by long-running functions to avoid blocking the event loop for the full duration of the function call.
#
# Example of coroutine displaying the current date every second for 5 seconds:
#
# """
#
#
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