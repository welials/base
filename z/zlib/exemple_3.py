import zlib, os

# создадим декомпрессор
unpack = zlib.decompressobj()

# открываем файлы на чтение 'sample.zl' и запись
#  'unpack-sample.txt' - оба в бинарных режимах.
with open('sample.zl', 'rb') as fpr, \
     open('unpack-sample.txt', 'wb') as fpw:
    while True:
        # читаем частями по 32 байта
        block = fpr.read(32)
        if block:
            # распаковываем
            data = unpack.decompress(block)
            # пишем данные ф текстовый файл
            fpw.write(data)
        else:
            break

# смотрим что получилось
print(os.system("file 'unpack-sample.txt'")) # unpack-sample.txt: UTF-8 Unicode text, with very long lines