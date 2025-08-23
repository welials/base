import zipfile, glob

extract_dir = 'extract_dir'

with zipfile.ZipFile('test.zip') as zf:
    zf.extractall(extract_dir)

for file in glob.glob(extract_dir + '/**', recursive=True):
    print(file)

# extract_dir\PycharmProjects\Base
# extract_dir\PycharmProjects\Base\z
# extract_dir\PycharmProjects\Base\z\zipfile
# extract_dir\PycharmProjects\Base\z\zipfile\exemple_1.py
# extract_dir\PycharmProjects\Base\z\zipfile\exemple_2.py
# extract_dir\PycharmProjects\Base\z\zipfile\exemple_3.py
# extract_dir\PycharmProjects\Base\z\zipfile\test.zip
# extract_dir\script-add.sql