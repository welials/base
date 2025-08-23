import zipfile, os

path = os.getcwd()
file_dir = os.listdir(path)
# crete .zip
with zipfile.ZipFile('test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(path, file)
        zf.write(add_file)

print(os.system('file test.zip')) # test.zip: Zip archive data, at least v2.0 to extract

# for add file
add_file = os.getcwd()+'/.py'

with zipfile.ZipFile('test.zip', mode='a', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(add_file, arcname='script-add.sql')

