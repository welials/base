import argparse


"""
The add_subparsers() method also supports title and description keyword arguments. 
When either is present, the subparser’s commands will appear in their own group in the help output. For example:
"""
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='additional help')
subparsers.add_parser('foo')
subparsers.add_parser('bar')
parser.parse_args(['-h'])
"""
usage:  [-h] {foo,bar} ...

options:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help
"""
"""
Furthermore, add_parser() supports an additional aliases argument, 
which allows multiple strings to refer to the same subparser. 
This example, like svn, aliases co as a shorthand for checkout:
"""

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
checkout = subparsers.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')
parser.parse_args(['co', 'bar'])
"""
Namespace(foo='bar')
"""
"""
add_parser()поддерживает также дополнительный устаревший аргумент, позволяющий отменить подпарсер.
"""

import argparse
parser = argparse.ArgumentParser(prog='chicken.py')
subparsers = parser.add_subparsers()
run = subparsers.add_parser('run')
fly = subparsers.add_parser('fly', deprecated=True)
parser.parse_args(['fly'])
"""
chicken.py: warning: command 'fly' is deprecated
Namespace()
"""
"""
One particularly effective way of handling subcommands is to combine the use of the add_subparsers() 
method with calls to set_defaults() so that each subparser knows which Python function it should execute. For example:
"""

# subcommand functions
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args = parser.parse_args('foo 1 -x 2'.split())
args.func(args)
"""
2.0
"""
# parse the args and call whatever function was selected
args = parser.parse_args('bar XYZYX'.split())
args.func(args)
"""
((XYZYX))
"""
"""
This way, you can let parse_args() do the job of calling the appropriate function 
after argument parsing is complete. Associating functions with actions like this is typically 
the easiest way to handle the different actions for each of your subparsers. 
However, if it is necessary to check the name of the subparser that was invoked, 
the dest keyword argument to the add_subparsers() call will work:
"""

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')
subparser1 = subparsers.add_parser('1')
subparser1.add_argument('-x')
subparser2 = subparsers.add_parser('2')
subparser2.add_argument('y')
parser.parse_args(['2', 'frobble'])
"""
Namespace(subparser_name='2', y='frobble')
"""