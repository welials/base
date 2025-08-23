import zlib

# создадим массив данных
text = 'Привет docs-python.ru '
data = []
for _ in range(10):
    data.append(text * 20)
# преобразование текста в байты

byte_data = '\n\n'.join(data).encode('utf-8')  # сжимаем данные
compress = zlib.compress(byte_data, level=-1)  # длинна не сжатых данных
print(len(byte_data))  # 4418
# длинна сжатых данных
print(len(compress))  # 85

# найдем процент сжатия
print(len(compress) / len(byte_data))  # 0.01923947487550928
# распаковываем сжатые 'compress' из буфера
decompress = zlib.decompress(compress)
# преобразуем байты в текст
text = decompress.decode('utf-8')
# выведем на печать первые 22 символа
print(text[0:22])  # 'Привет docs-python.ru Привет'
