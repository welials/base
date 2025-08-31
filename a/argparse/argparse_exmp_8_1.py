import argparse
# type
"""
By default, the parser reads command-line arguments in as simple strings. 
However, quite often the command-line string should instead be interpreted as another type, such as a float or int. 
The type keyword for add_argument() allows any necessary type-checking and type conversions to be performed.
"""
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('count', type=int)
parser.add_argument('distance', type=float)
parser.add_argument('street', type=ascii)
parser.add_argument('code_point', type=ord)
parser.add_argument('dest_file', type=argparse.FileType('w', encoding='latin-1'))
parser.add_argument('datapath', type=pathlib.Path)
parser.print_help()
"""
User defined functions can be used as well:
"""
print("#"*100)
def hyphenated(string):
    return '-'.join([word[:4] for word in string.casefold().split()])

parser = argparse.ArgumentParser()
_ = parser.add_argument('short_title', type=hyphenated)
print(parser.parse_args(['"The Tale of Two Cities"']))
"""
Namespace(short_title='"the-tale-of-two-citi')
"""
