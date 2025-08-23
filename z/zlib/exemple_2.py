
import zlib, pprint, binascii, os

# подготовим данные
text = 'Привет docs-python.ru '
data = []
for _ in range(50):
    data.append(text * 25)

# запишем данные в файл
with open('sample.txt', 'w') as fp:
    fp.write('\n\n'.join(data))

# создадим объекта сжатия `Compress`
compressor = zlib.compressobj(1)

# открываем созданный файл в двоичном
# режиме, читаем блоками и сжимаем
with open('sample.txt', 'rb') as fp, \
        open('sample.zl', 'wb') as fz:
    while True:
        block = fp.read(4096)
        if block:
            # сжимаем
            compressed = compressor.compress(block)
            if compressed:
                print(f'Compressed: {binascii.hexlify(compressed)}')
                # пишем
                fz.write(compressed)
            else:
                print('buffering...')
        else:
            break
    # данные кончились, сбросим буфер
    # и запишем остатки
    remaining = compressor.flush()
    fz.write(remaining)
    print('Flushed:')
    pprint.pprint(binascii.hexlify(remaining), width=60)

# Compressed: b'7801'
# buffering...
# buffering...
# buffering...
# buffering...
# buffering...
# buffering...
# Flushed:
# (b'edd8b10dc2501403c03e536402e648c90c8c8094820eb1083b202131'
#  b'c6cf4669e9e2c24a752de5d7d9cf61bcb7e7f88dcff86eaff9fa58d6'
#  b'dbe5becec3afdee1cfc334112119c70dc189064d2e09279c70e2a6b6'
#  b'6eaa3ed127fa449fe89324059c70c2c999ff7bd927f64992384e38e1'
#  b'c43eb14f921470c20927766c2b05faa4f59276ac1d9b3433279c70e2'
#  b'eeb83b490a38e18413df3bad14e893d64bdab1766cd2cc9c70c289bb'
#  b'e3ee2429e084134e7cefb452a04f5a2f69c7dab1493373c20927ee8e'
#  b'bb93a480134e38f1bdd34a813e69bda41d6bc726cdcc09279cb83bee'
#  b'4e92024e38e1c4f74e2b05faa4f59276ac1d9b3433279c70e2eeb83b'
#  b'490a38e18413df3bad14e893d64bdab1766cd2cc9c70c289bbe3ee24'
#  b'29e084134ecefcded901ec6bfe0a')

print(os.system(f'file sample.zl')) # sample.zl: zlib compressed data
print(os.path.getsize('sample.txt')) # 27598
print(os.path.getsize('sample.zl')) # 294