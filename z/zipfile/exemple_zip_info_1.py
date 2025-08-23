import zipfile, os, time
file = 'test.csv'
# структура времени файла
file_time_tuple = time.localtime(os.path.getmtime(file))
zf_file = zipfile.ZipInfo(file, file_time_tuple).from_file(file)
print(zf_file.is_dir()) # False
print(zf_file.filename) # test.csv
print(zf_file.date_time) # (2020, 5, 18, 13, 21, 43)
print(zf_file.compress_type) # 0
zf_file.compress_type = zipfile.ZIP_DEFLATED
print(zf_file.compress_type) # 8
zf_file.comment = b'Comment'
zf_file.comment