import argparse
# nargs
"""
'*'. All command-line arguments present are gathered into a list. 
Note that it generally doesn’t make much sense to have more than one positional argument with nargs='*', 
but multiple optional arguments with nargs='*' is possible. For example:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')
parser.add_argument('--bar', nargs='*')
parser.add_argument('baz', nargs='*')
print(parser.parse_args('a b --foo x y --bar 1 2'.split()))
"""
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
"""