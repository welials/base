# A Conceptual Overview of asyncio

# Внутренняя работа сопрограмм
"""
asyncio использует четыре компонента для передачи управления.

coroutine.send(arg)— это метод, используемый для запуска или возобновления сопрограммы. Если сопрограмма была приостановлена ​​и теперь возобновляется, аргумент arg будет передан как возвращаемое значение оператора yield, который изначально её приостановил. Если сопрограмма используется впервые (а не возобновляется), argнеобходимо указать None.
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
try:
    coroutine.send(42)
except StopIteration as e:
    returned_value = e.value
print(f"Coroutine main() finished and provided value: {returned_value}.")
"""
yield , как обычно, приостанавливает выполнение и возвращает управление вызывающему объекту. В приведенном выше примере метод yieldyieldв строке 3 вызывается методом в строке 11. В более широком смысле,он вызываетметод заданного объекта. Также выполняет ещё одну весьма специфичную функцию: распространяет (или «передаёт») любойполученный им объект s по цепочке вызовов. В данном случае это происходитв строке 16.... = await rockawait__await__()awaityield... = coroutine.send(None)

Выполнение сопрограммы возобновляется coroutine.send(42)вызовом в строке 21. Сопрограмма возобновляет выполнение с того места, где она yieldостановилась (или была приостановлена) в строке 3, и выполняет оставшиеся операторы в своём теле. После завершения сопрограммы возникает StopIterationисключение с возвращаемым значением, прикреплённым к valueатрибуту.

Этот фрагмент выводит следующий результат:

Beginning coroutine main().
Awaiting rock...
Coroutine paused and returned intermediate value: 7.
Resuming coroutine and sending in value: 42.
Rock.__await__ resuming with value: 42.
Coroutine received value: 42 from rock.
Coroutine main() finished and provided value: 23.
Здесь стоит на мгновение остановиться и убедиться, что вы проследили все способы передачи управляющего потока и значений. Было рассмотрено много важных идей, и стоит убедиться, что вы всё хорошо поняли.

Единственный способ передать управление (или фактически передать управление) сопрограмме — это awaitобъекту, yieldнаходящемуся в её __await__методе. Это может показаться вам странным. Вы можете подумать:

1. А как насчёт yieldфункции непосредственно внутри сопрограммы? Функция сопрограммы становится функцией асинхронного генератора , что совершенно не похоже на оригинал.

2. Что насчёт передачи управления из функции сопрограммы (обычному) генератору? Это приводит к ошибке: это было намеренно разработано для простоты — предписывая только один способ использования сопрограмм. Изначально это также было запрещено, но затем снова принято, чтобы разрешить использование асинхронных генераторов. Несмотря на это, фактически это то же самое.SyntaxError: yield from not allowed in a coroutine.yieldyield from await
"""
