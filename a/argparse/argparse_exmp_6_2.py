import argparse, sys
# nargs
"""
?'. One argument will be consumed from the command line if possible, 
and produced as a single item. If no command-line argument is present, 
the value from default will be produced. Note that for optional arguments, 
there is an additional case - the option string is present but not followed by a command-line argument. 
In this case the value from const will be produced. Some examples to illustrate this:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?', default='d')
print(parser.parse_args(['XX', '--foo', 'YY']))
"""
Namespace(bar='XX', foo='YY')
"""
print(parser.parse_args(['XX', '--foo']))
"""
Namespace(bar='XX', foo='c')
"""
print(parser.parse_args([]))
"""
Namespace(bar='d', foo='d')
"""
print("#"*100)
"""
One of the more common uses of nargs='?' is to allow optional input and output files:
"""
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
print(parser.parse_args(['input.txt', 'output.txt']))
"""
Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
"""
print(parser.parse_args([]))
"""
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)
"""