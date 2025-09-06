import array

print(array.array('l'))
print(array.array('w', 'hello \u2641'))
print(array.array('l', [1, 2, 3, 4, 5]))
print(('d', [1.0, 2.0, 3.14]))
"""
array.typecode:
Свойство array.typecode возвращает символ typecode, используемый для создания массива array.
"""
arr = array.array('i', range(3))

print(arr.typecode)
# 'i'

print(arr)
# array('i', [0, 1, 2])
"""
array.itemsize:
Свойство array.itemsize возвращает длину в байтах одного элемента массива array во внутреннем представлении.
"""
arr = array.array('i', range(3))
print(arr.itemsize)
# 4
print(arr)
# array('i', [0, 1, 2])
"""
array.append(x):
Метод array.append() добавляет новый элемент со значением x в конец массива array.
"""

>>> import array
>>> arr = array.array('i', range(3))
>>> arr
# array('i', [0, 1, 2])

>>> arr.append(10)
>>> arr
# array('i', [0, 1, 2, 10])

array.buffer_info():
Метод array.buffer_info() возвращает кортеж (address, length) с текущим адресом памяти address и длиной length в элементах буфера, используемых для хранения содержимого массива. Размер буфера памяти в байтах может быть получен как array.buffer_info()[1] * array.itemsize. Это иногда полезно при работе с низкоуровневыми и небезопасными интерфейсами ввода-вывода, которым требуются адреса памяти, такие как определенные операции ioctl(). Возвращенные числа действительны до тех пор, пока существует массив и к нему не применяются операции с изменением длины.

Примечание. При использовании объектов массива из кода, написанного на C или C++, имеет смысл использовать интерфейс буфера, поддерживаемый объектами массива. Этот метод поддерживается для обратной совместимости и его следует избегать в новом коде. Интерфейс буфера задокументирован в Buffer Protocol.

>>> import array
>>> arr = array.array('i', range(4))
>>> arr
# array('i', [0, 1, 2, 3])

>>> arr.buffer_info()
# (139650602648528, 4)

# Размер буфера памяти
size_buf = arr.itemsize * arr.buffer_info()[1]
>>> size_buf
# 16

array.byteswap():
Метод array.byteswap() меняет порядок байтов каждого элемента в массиве . Метод поддерживает только значения размером 1, 2, 4 или 8 байт. Для других типов значений вызывается исключение RuntimeError.

Метод array.byteswap() полезно использовать при чтении данных из файла, записанного на машине с другим порядком байтов.

>>> import array
>>> arr = array.array('i', range(4))
>>> arr
# array('i', [0, 1, 2, 3])

>>> arr.byteswap()
>>> arr
# array('i', [0, 16777216, 33554432, 50331648])

array.count(x):
Метод array.count() вернет количество вхождений аргумента x в массиве array.

>>> import array
>>> arr = array.array('i', range(4))
>>> arr.extend([1,1])
>>> arr.count(1)
# 3

>>> arr
# array('i', [0, 1, 2, 3, 1, 1])


tbank.ru
Реклама
Получите 50 ГБ
интернета
и безлимитные
звонки за 390 ₽
Перенесите свой номер
в Т-Мобайл до 30
сентября, и нового тарифа
хватит на всё.
Подробнее
array.extend(iterable):
Метод array.extend() добавляет элементы из итерируемого объекта iterable в конец массива array.

Если iterable - это другой массив array, он должен иметь точно такой же typecode. Если typecode другой, то появится исключение TypeError. Если iterable не является массивом array, то он должен быть повторяемым, а его элементы должны иметь правильный тип для добавления в массив.

>>> import array
>>> arr = array.array('i', range(4))
>>> arr.extend([10,11])
>>> arr
# array('i', [0, 1, 2, 3, 10, 11])

array.frombytes(s):
Метод array.frombytes() добавляет элементы из строки, интерпретируя строку как массив машинных значений. Как если бы она была прочитана из файла с помощью метода array.fromfile().

>>> import array
>>> arr = array.array('i', range(4))
>>> line = arr.tobytes()
>>> line
# b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'

>>> arr1 = array.array('i')
>>> arr1.frombytes(line)
>>> arr1
# array('i', [0, 1, 2, 3])

array.fromfile(fp, n):
Метод array.fromfile() считывает n элементов (как машинные значения) из файлового объекта fp и добавляет их в конец массива.

Если доступно менее n элементов, вызывается исключение EOFError, но при этом доступные элементы вставляются в массив. Аргумент fp должен быть настоящим файловым объектом. Для чтения массива из фала метод file.read() не подойдет.

Смотрите пример использования в разделе "Сохранение/чтение массива array() в/из файл(а)".


array.fromlist(list):
Метод array.fromlist() добавляет элементы массив array из списка list. Это эквивалентно добавлению x в список array.append(x), за исключением того, что в случае ошибки типа массив array не изменяется.

>>> import array
>>> arr = array.array('i', range(2))
>>> arr.fromlist([10,20,30,40])
>>> arr
# array('i', [0, 1, 10, 20, 30, 40])

array.fromunicode(s):
Метод array.fromunicode() расширяет массив array данными из заданной строки s в Unicode. Массив array должен быть массивом типа 'u', в противном случае поднимается исключение ValueError.

Используйте array.frombytes(unicodestring.encode(enc)), чтобы добавить данные Unicode в массив другого типа.

>>> import array
>>> arr = array.array('u', 'string')
>>> arr
# array('u', 'string')

>>> arr.fromunicode('string2')
>>> arr
# array('u', 'stringstring2')

array.index(x[, start[, stop]]):
Метод array.index() возвращает наименьшее целое число i, где i является индексом первого вхождения значения x в массив array.

Необязательные аргументы start и stop (доступны с Python 3.10) могут быть указаны для поиска x в части массива. Поднимает ValueError, если x не найден.

>>> import array
>>> arr = array.array('i', range(3))
>>> arr.fromlist([1, 1, 4])
>>> arr.index(1)
# 1

>>> arr
array('i', [0, 1, 2, 1, 1, 4])
Изменено в версии 3.10: Добавлены необязательные аргументы start и stop.



dodopizza.ru
Реклама
Быстрая и надежная
доставка Додо
Пицца
Горячая вкусная еда
приедет вовремя
Заказать
array.insert(i, x):
Метод array.insert() вставляет новый элемент со значением x в массив array перед позицией i. Отрицательные значения рассматриваются как относящиеся к концу массива.

>>> import array
>>> arr = array.array('i', range(3))
>>> arr
# array('i', [0, 1, 2])

>>> arr.insert(1, 2)
>>> arr
# array('i', [0, 2, 1, 2])

array.pop([i]):
Метод array.pop() удаляет элемент с индексом i из массива array и возвращает его. Необязательный аргумент индекса i массива array по умолчанию равен -1. По умолчанию удаляется и возвращается последний элемент массива array.

>>> import array
>>> arr = array.array('i', range(2,6))
>>> arr.pop()
# 5
>>> arr.pop(1)
# 3
>>> arr
# array('i', [2, 4])

array.remove(x):
Метод array.remove() удаляет первое вхождение значения аргумента x из массива array.

>>> import array
>>> arr = array.array('i', range(2,6))
>>> arr.fromlist([3, 3])
>>> arr
# array('i', [2, 3, 4, 5, 3, 3])
>>> arr.remove(3)
>>> arr
array('i', [2, 4, 5, 3, 3])

array.reverse():
Метод array.reverse() переворачивает массив array. Другими словами обеспечивает обратный порядок элементов в массиве.

>>> import array
>>> arr = array.array('i', range(2,6))
>>> arr.reverse()
>>> arr
# array('i', [5, 4, 3, 2])

array.tobytes():
Метод array.tobytes() преобразует массив array в массив машинных значений и вернет представление байтов - ту же последовательность байтов, которая была бы записана в файл методом array.tofile().

>>> import array
>>> arr = array.array('i', range(4))
>>> line = arr.tobytes()
>>> line
# b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'

array.tofile(fp):
Метод array.tofile() записывает все элементы массива array (как машинные значения) в объект файла fp.

Смотрите пример использования в разделе "Сохранение/чтение массива array() в/из файл(а)".


array.tolist():
Метод array.tolist() преобразует массив array в обычный список с теми же элементами.

>>> import array
>>> arr = array.array('i', range(4))
>>> arr.tolist()
# [0, 1, 2, 3]

array.tounicode():
Метод array.tounicode() преобразует массив array в строку Unicode. Массив должен быть массивом типа 'u'. В противном случае возникает ошибка ValueError. Используйте array.tobytes().decode(enc) для получения строки Unicode из массива другого типа.

>>> import array
>>> arr = array.array('u', 'the string')
>>> arr.tounicode()
# 'the string'