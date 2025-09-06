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
arr = array.array('i', range(3))
print(arr)
# array('i', [0, 1, 2])

arr.append(10)
print(arr)
# array('i', [0, 1, 2, 10])
"""
array.buffer_info():
Метод array.buffer_info() возвращает кортеж (address, length) с текущим 
адресом памяти address и длиной length в элементах буфера, используемых для хранения содержимого массива. 
Размер буфера памяти в байтах может быть получен как array.buffer_info()[1] * array.itemsize. 
Это иногда полезно при работе с низкоуровневыми и небезопасными интерфейсами ввода-вывода, 
которым требуются адреса памяти, такие как определенные операции ioctl(). 
Возвращенные числа действительны до тех пор, пока существует массив и к нему не применяются операции с изменением длины.

Примечание. При использовании объектов массива из кода, написанного на C или C++, 
имеет смысл использовать интерфейс буфера, поддерживаемый объектами массива. 
Этот метод поддерживается для обратной совместимости и его следует избегать в новом коде. 
Интерфейс буфера задокументирован в Buffer Protocol.
"""

arr = array.array('i', range(4))
print(arr)
# array('i', [0, 1, 2, 3])

print(arr.buffer_info())
# (139650602648528, 4)

# Размер буфера памяти
size_buf = arr.itemsize * arr.buffer_info()[1]
print(size_buf)
# 16
