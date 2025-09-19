import asyncio

# A conceptual overview part 2: the nuts and bolts
"""
# Концептуальный обзор, часть 2: гайки и болты 

Во второй части подробно рассматриваются механизмы asyncio управления потоком управления. 
Именно здесь и происходит волшебство. Вы получите представление о том, что await
происходит за кулисами, и о том, как создавать собственные асинхронные операторы.

Внутренняя работа сопрограмм asyncio использует четыре компонента для передачи управления.
"""
"""
coroutine.send(arg)— это метод, используемый для запуска или возобновления сопрограммы. 
Если сопрограмма была приостановлена и теперь возобновляется, 
аргумент arg будет передан как возвращаемое значение оператора yield, 
который изначально её приостановил. Если сопрограмма используется впервые (а не возобновляется), 
arg необходимо указать None.
"""
class Rock:
    def __await__(self):
        value_sent_in = yield 7
        print(f"Rock.__await__ resuming with value: {value_sent_in}.")
        return value_sent_in

async def main():
    print("Beginning coroutine main().")
    rock = Rock()
    print("Awaiting rock...")
    value_from_rock = await rock
    print(f"Coroutine received value: {value_from_rock} from rock.")
    return 23

coroutine = main()
intermediate_result = coroutine.send(None)
print(f"Coroutine paused and returned intermediate value: {intermediate_result}.")

print(f"Resuming coroutine and sending in value: 42.")
returned_value = None
try:
    coroutine.send(42)
except StopIteration as e:
    returned_value = e.value
print(f"Coroutine main() finished and provided value: {returned_value}.")
"""
yield , как обычно, приостанавливает выполнение и возвращает управление вызывающему объекту. В приведенном выше примере метод yieldyieldв строке 3 вызывается методом в строке 11. В более широком смысле,он вызываетметод заданного объекта. Также выполняет ещё одну весьма специфичную функцию: распространяет (или «передаёт») любойполученный им объект s по цепочке вызовов. В данном случае это происходитв строке 16.... = await rockawait__await__()awaityield... = coroutine.send(None)

Выполнение сопрограммы возобновляется coroutine.send(42)вызовом в строке 21. Сопрограмма возобновляет выполнение с того места, где она yieldостановилась (или была приостановлена) в строке 3, и выполняет оставшиеся операторы в своём теле. После завершения сопрограммы возникает StopIterationисключение с возвращаемым значением, прикреплённым к valueатрибуту.

Этот фрагмент выводит следующий результат:
"""
# Beginning coroutine main().
# Awaiting rock...
# Coroutine paused and returned intermediate value: 7.
# Resuming coroutine and sending in value: 42.
# Rock.__await__ resuming with value: 42.
# Coroutine received value: 42 from rock.
# Coroutine main() finished and provided value: 23.
"""
Единственный способ передать управление (или фактически передать управление) сопрограмме — это дождаться объекта, 
который возвращает управление в своём методе __await__. Это может показаться вам странным. 
Вы можете подумать:

1. А что насчёт yield непосредственно внутри функции сопрограммы? 
Функция сопрограммы становится асинхронной функцией-генератором, и это совсем другое дело.

2. А что насчёт yield from внутри функции сопрограммы к (обычному) генератору? 
Это приводит к ошибке: SyntaxError: yield from not allowed in a coroutine. 
Это было сделано намеренно для простоты — предписывая только один способ использования сопрограмм. 
Изначально yield также был запрещён, 
но был вновь принят для разрешения асинхронных генераторов. 
Несмотря на это, yield from и await фактически делают одно и то же.
"""

# Фьючерсы

"""
Future — это объект, предназначенный для представления состояния и результата вычисления. 
Этот термин отсылает к идее чего-то , что ещё должно произойти или ещё не произошло, и объект — это способ следить за этим.
У будущего есть несколько важных атрибутов. Один из них — его состояние, 
которое может быть «ожидание», «отменено» или «выполнено». 
Другой — его результат, который устанавливается при переходе состояния в «выполнено». 
В отличие от сопрограммы, будущее не представляет фактическое вычисление, которое должно быть выполнено; 
вместо этого оно отображает статус и результат этого вычисления, своего рода индикатор состояния (красный, жёлтый или зелёный).

asyncio.Task Подклассы asyncio.Future для получения этих разнообразных возможностей. 
В предыдущем разделе говорилось, что задачи хранят список обратных вызовов, 
что было не совсем верно. На самом деле Future эту логику реализует класс, который Task наследует.

Фьючерсы также можно использовать напрямую (не через задачи). Задачи отмечают себя как выполненные после завершения своей сопрограммы. Фьючерсы гораздо более универсальны и будут отмечены как выполненные, когда вы этого захотите. Таким образом, они представляют собой гибкий интерфейс для создания собственных условий ожидания и возобновления.

Самодельный asyncio.sleep 
Мы рассмотрим пример того, как вы можете использовать будущее для создания собственного варианта асинхронного сна ( async_sleep), который имитирует asyncio.sleep().

Этот фрагмент регистрирует несколько задач в цикле событий, а затем ожидает сопрограмму, обёрнутую в задачу: async_sleep(3). Мы хотим, чтобы эта задача завершилась только по истечении трёх секунд, но без остановки выполнения других задач.

async def other_work():
    print("I like work. Work work.")

async def main():
    # Add a few other tasks to the event loop, so there's something
    # to do while asynchronously sleeping.
    work_tasks = [
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work()),
        asyncio.create_task(other_work())
    ]
    print(
        "Beginning asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    await asyncio.create_task(async_sleep(3))
    print(
        "Done asynchronous sleep at time: "
        f"{datetime.datetime.now().strftime("%H:%M:%S")}."
    )
    # asyncio.gather effectively awaits each task in the collection.
    await asyncio.gather(*work_tasks)
Ниже мы используем будущий объект, чтобы настроить управление моментом, когда задача будет отмечена как выполненная. Если future.set_result()метод, отвечающий за отметку будущего объекта как выполненного, никогда не будет вызван, то эта задача никогда не завершится. Мы также заручились помощью другой задачи, которую мы увидим чуть позже, которая будет отслеживать прошедшее время и, соответственно, вызывать future.set_result().

async def async_sleep(seconds: float):
    future = asyncio.Future()
    time_to_wake = time.time() + seconds
    # Add the watcher-task to the event loop.
    watcher_task = asyncio.create_task(_sleep_watcher(future, time_to_wake))
    # Block until the future is marked as done.
    await future
Ниже мы используем довольно простой объект , YieldToEventLoop()чтобы yield передать __await__управление циклу событий. По сути, это то же самое, что вызвать asyncio.sleep(0), но такой подход обеспечивает большую ясность, не говоря уже о том, что это несколько нечестно asyncio.sleepпри демонстрации реализации!

Как обычно, цикл событий циклически проходит через свои задачи, передавая им управление и получая его обратно, когда они приостанавливаются или завершаются. watcher_task, который запускает сопрограмму _sleep_watcher(...), будет вызываться один раз за полный цикл цикла событий. При каждом возобновлении он будет проверять время, и если прошло недостаточно времени, то он снова приостановится и передаст управление обратно циклу событий. В конце концов, когда пройдет достаточно времени, _sleep_watcher(...)будущая задача будет отмечена как выполненная, а затем сама завершится, вырвавшись из бесконечного whileцикла. Учитывая, что эта вспомогательная задача вызывается только один раз за цикл цикла событий, вы будете правы, заметив, что этот асинхронный сон будет спать не менее трех секунд, а не ровно три. Обратите внимание, что это также верно для asyncio.sleep.

class YieldToEventLoop:
    def __await__(self):
        yield

async def _sleep_watcher(future, time_to_wake):
    while True:
        if time.time() >= time_to_wake:
            # This marks the future as done.
            future.set_result(None)
            break
        else:
            await YieldToEventLoop()
Вот полный вывод программы:

$ python custom-async-sleep.py
Beginning asynchronous sleep at time: 14:52:22.
I like work. Work work.
I like work. Work work.
I like work. Work work.
Done asynchronous sleep at time: 14:52:25.
Вам может показаться, что эта реализация асинхронного сна излишне запутана. И, по сути, так оно и есть. Целью этого примера было продемонстрировать универсальность фьючерсов на простом примере, который можно было бы использовать для более сложных задач. Для справки, вы можете реализовать это без фьючерсов, например, так:

async def simpler_async_sleep(seconds):
    time_to_wake = time.time() + seconds
    while True:
        if time.time() >= time_to_wake:
            return
        else:
            await YieldToEventLoop()
Но на этом всё. Надеюсь, вы готовы более уверенно погрузиться в асинхронное программирование или изучить более сложные темы в .rest of the documentation
"""