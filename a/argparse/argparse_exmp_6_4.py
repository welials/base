import argparse
# nargs
"""
'+'. Just like '*', all command-line arguments present are gathered into a list. 
Additionally, an error message will be generated if there wasn’t at least one command-line argument present. For example:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', nargs='+')
print(parser.parse_args(['a', 'b']))
"""
Namespace(foo=['a', 'b'])
"""
print(parser.parse_args([]))
"""
usage: PROG [-h] foo [foo ...]
PROG: error: the following arguments are required: foo
"""