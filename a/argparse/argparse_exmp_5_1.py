import argparse
"""
name or flags
The add_argument() method must know whether an optional argument, like -f or --foo, or a positional argument, like a list of filenames, is expected. The first arguments passed to add_argument() must therefore be either a series of flags, or a simple argument name.

For example, an optional argument could be created like:
parser.add_argument('-f', '--foo')
while a positional argument could be created like:
parser.add_argument('bar')
When parse_args() is called, optional arguments will be identified by the - prefix, and the remaining arguments will be assumed to be positional:
"""

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo')
parser.add_argument('bar')
parser.parse_args(['BAR'])
parser.print_help()
"""
Namespace(bar='BAR', foo=None)
"""
print("#"*100)
parser.parse_args(['BAR', '--foo', 'FOO'])
parser.print_help()
"""
Namespace(bar='BAR', foo='FOO')
"""
print("#"*100)
parser.parse_args(['--foo', 'FOO'])
parser.print_help()
"""
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar
"""