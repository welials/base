import argparse
"""
'store_true' and 'store_false' - These are special cases of 'store_const'
 used for storing the values True and False respectively. 
In addition, they create default values of False and True respectively:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
parser.parse_args('--foo --bar'.split())
parser.print_help()
"""
Namespace(foo=True, bar=False, baz=True)
"""