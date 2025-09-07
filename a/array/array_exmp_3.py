import array
"""
array.fromunicode(s):
Метод array.fromunicode() расширяет массив array данными из заданной строки s в Unicode. 
Массив array должен быть массивом типа 'u', в противном случае поднимается исключение ValueError.

Используйте array.frombytes(unicodestring.encode(enc)), чтобы добавить данные Unicode в массив другого типа.
"""

arr = array.array('w', 'string') # u - DeprecationWarning arr = array.array('u', 'string')
print(arr)
# array('u', 'string')

arr.fromunicode('string2')
print(arr)
# array('u', 'stringstring2')
"""
array.index(x[, start[, stop]]):
Метод array.index() возвращает наименьшее целое число i, где i 
является индексом первого вхождения значения x в массив array.

Необязательные аргументы start и stop (доступны с Python 3.10) 
могут быть указаны для поиска x в части массива. Поднимает ValueError, если x не найден.
"""

arr = array.array('i', range(3))
arr.fromlist([1, 1, 4])
print(arr.index(1))
# 1

print(arr)
# array('i', [0, 1, 2, 1, 1, 4])

"""
array.insert(i, x):
Метод array.insert() вставляет новый элемент со значением x в массив array перед позицией i. 
Отрицательные значения рассматриваются как относящиеся к концу массива.
"""

arr = array.array('i', range(3))
print(arr)
# array('i', [0, 1, 2])

arr.insert(1, 2)
print(arr)
# array('i', [0, 2, 1, 2])
"""
array.pop([i]):
Метод array.pop() удаляет элемент с индексом i из массива array и возвращает его. 
Необязательный аргумент индекса i массива array по умолчанию равен -1. 
По умолчанию удаляется и возвращается последний элемент массива array.
"""

arr = array.array('i', range(2,6))
print(arr.pop())
# 5
print(arr.pop(1))
# 3
print(arr)
# array('i', [2, 4])
"""
array.remove(x):
Метод array.remove() удаляет первое вхождение значения аргумента x из массива array.
"""

arr = array.array('i', range(2,6))
arr.fromlist([3, 3])
print(arr)
# array('i', [2, 3, 4, 5, 3, 3])
arr.remove(3)
print(arr)
# array('i', [2, 4, 5, 3, 3])
