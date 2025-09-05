import argparse

"""
Other utilities
Sub-commands
ArgumentParser.add_subparsers(*[, title][, description][, prog][, parser_class][, action][, dest][, required][, help][, metavar])
Many programs split up their functionality into a number of subcommands, for example, the svn program can invoke subcommands like svn checkout, 
svn update, and svn commit. Splitting up functionality this way can be a particularly good idea when a program performs several 
different functions which require different kinds of command-line arguments. ArgumentParser supports the creation of such subcommands 
with the add_subparsers() method. The add_subparsers() method is normally called with no arguments and returns a special action object. 
This object has a single method, add_parser(), which takes a command name and any ArgumentParser constructor arguments, and returns an 
ArgumentParser object that can be modified as usual.

Description of parameters:

title - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments

description - description for the sub-parser group in help output, by default None

prog - usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments 
before the subparser argument

parser_class - class which will be used to create sub-parser instances, by default the class of the current parser (e.g. ArgumentParser)

action - the basic type of action to be taken when this argument is encountered at the command line

dest - name of the attribute under which sub-command name will be stored; by default None and no value is stored

required - Whether or not a subcommand must be provided, by default False (added in 3.7)

help - help for sub-parser group in help output, by default None

metavar - string presenting available subcommands in help; by default it is None and presents subcommands in form {cmd1, cmd2, ..}
Some example usage:
"""
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='subcommand help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')

# parse some argument lists
print(parser.parse_args(['a', '12']))
"""
Namespace(bar=12, foo=False)
"""
print(parser.parse_args(['--foo', 'b', '--baz', 'Z']))
"""
Namespace(baz='Z', foo=True)
"""
"""
Note that the object returned by parse_args() will only contain attributes for the main 
parser and the subparser that was selected by the command line (and not any other subparsers). 
So in the example above, when the a command is specified, only the foo and bar attributes are present, 
and when the b command is specified, only the foo and baz attributes are present.

Note that the object returned by parse_args() will only contain attributes for the main parser and the 
subparser that was selected by the command line (and not any other subparsers). So in the example above, 
when the a command is specified, only the foo and bar attributes are present, and when the b command is specified, 
only the foo and baz attributes are present.

Similarly, when a help message is requested from a subparser, 
only the help for that particular parser will be printed. 
The help message will not include parent parser or sibling parser messages. 
(A help message for each subparser command, however, 
can be given by supplying the help= argument to add_parser() as above.)

"""
print(parser.parse_args(['--help']))

"""
usage: PROG [-h] [--foo] {a,b} ...

positional arguments:
  {a,b}   subcommand help
    a     a help
    b     b help

options:
  -h, --help  show this help message and exit
  --foo   foo help
"""

print(parser.parse_args(['a', '--help']))
"""
usage: PROG a [-h] bar

positional arguments:
  bar     bar help

options:
  -h, --help  show this help message and exit
"""
print(parser.parse_args(['b', '--help']))
"""
usage: PROG b [-h] [--baz {X,Y,Z}]

options:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help
"""