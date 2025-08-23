import zipfile, os

# list file in .zip
with zipfile.ZipFile('test.zip', mode='a') as zf:
    for file in zf.namelist():
        print(file)

# ditail information in .zip

import zipfile, datetime

with zipfile.ZipFile('test.zip', mode='a') as zf:
    for file in zf.infolist():
        # дата файла в архиве
        date = datetime.datetime(*file.date_time)
        # имя файла в архиве без пути
        name = os.path.basename(file.filename)
        # печатаем имя, начальный размер,
        # размер в архиве, дата файла
        print(f"{name},\t{file.file_size},\t{file.compress_size},\t \
                               {date.strftime('%H:%M %d.%m.%Y')}")