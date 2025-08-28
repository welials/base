"""
Модуль atexit определяет функции для регистрации и отмены регистрации функций очистки.
Зарегистрированные таким образом функции автоматически
выполняются после обычного завершения интерпретатора.
Модуль atexit запускает эти функции в обратном порядке, в котором они были зарегистрированы.
Если вы зарегистрируете A, B и C, во время завершения работы программы
они будут выполняться в порядке C, B, A.
функции, зарегистрированные через этот модуль, не вызываются,
когда программа прерывается сигналом, не обработанным Python,
когда обнаружена фатальная внутренняя ошибка Python или когда вызывается os._exit().
"""


def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
print('66666666666')

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')

"""
66666666666
You are now leaving the Python sector.
Goodbye Donny, it was nice to meet you.
"""