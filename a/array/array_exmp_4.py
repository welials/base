import array
"""
array.reverse():
Метод array.reverse() переворачивает массив array. Другими словами обеспечивает обратный порядок элементов в массиве.
"""

arr = array.array('i', range(2,6))
arr.reverse()
print(arr)
# array('i', [5, 4, 3, 2])
"""
array.tobytes():
Метод array.tobytes() преобразует массив array в массив машинных значений и вернет представление байтов - 
ту же последовательность байтов, которая была бы записана в файл методом array.tofile().
"""
arr = array.array('i', range(4))
line = arr.tobytes()
print(line)
# b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
"""
array.tofile(fp):
Метод array.tofile() записывает все элементы массива array (как машинные значения) в объект файла fp.

array.tolist():
Метод array.tolist() преобразует массив array в обычный список с теми же элементами.
"""
arr = array.array('i', range(4))
print(arr.tolist())
# [0, 1, 2, 3]
"""
array.tounicode():
Метод array.tounicode() преобразует массив array в строку Unicode. 
Массив должен быть массивом типа 'u'. В противном случае возникает ошибка ValueError. 
Используйте array.tobytes().decode(enc) для получения строки Unicode из массива другого типа.
"""
# DeprecationWarning
# arr = array.array('u', 'the string')
# arr = array.array('u', 'string')
# arr.tounicode()
arr = array.array('w', 'string')
arr.tounicode()