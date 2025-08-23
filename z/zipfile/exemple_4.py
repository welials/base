import zipfile, fnmatch, glob

# директория для извлечения
extract_dir = 'extract_dir'
# паттерн для извлечения файлов
file_pattern = '*.py'

with zipfile.ZipFile('test.zip') as zf:
    for file in zf.infolist():
        # выбираем файлы для извлечения по
        # 'file_pattern' и по объему в байтах
        if fnmatch.fnmatch(file.filename, file_pattern) \
                     and 2000 < file.file_size <= 3000:
            zf.extract(file.filename, extract_dir)

for file in glob.glob(extract_dir + '/**', recursive=True):
   print(file)