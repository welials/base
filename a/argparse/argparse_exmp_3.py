import argparse
"""
The base name of sys.argv[0] if a file was passed as argument.

The Python interpreter name followed by sys.argv[0] if a directory or a zipfile was passed as argument.

The Python interpreter name followed by -m followed by the module or package name if the -m option was used.

This default is almost always desirable because it will make the help messages match the string that was used to invoke the program on the command line. However, to change this default behavior, another value can be supplied using the prog= argument to ArgumentParser:
"""
# prog
parser = argparse.ArgumentParser(prog='myprogram')

parser.print_help()
"""
usage: myprogram [-h]
options:
 -h, --help  show this help message and exit
Note that the program name, whether determined from sys.argv[0] or from the prog= argument, is available to help messages using the %(prog)s format specifier.
"""
parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', help='foo of the %(prog)s program')
parser.print_help()
"""
usage: myprogram [-h] [--foo FOO]  <-- here myprogram

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
"""

# usage

"""
By default, ArgumentParser calculates the usage message from the arguments it contains. 
The default message can be overridden with the usage= keyword argument:
"""
parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
"""
usage: PROG [options] <-- here

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help 
The %(prog)s format specifier is available to fill in the program name in your usage messages.
"""
# description
"""
Most calls to the ArgumentParser constructor will use the description= keyword argument. 
This argument gives a brief description of what the program does and how it works. In help messages, 
the description is displayed between the command-line usage string and the help messages for the various arguments.

By default, the description will be line-wrapped so that it fits within the given space. To change this behavior, see the formatter_class argument.
"""
# epilog
"""
Some programs like to display additional description of the program after the description of the arguments.
Such text can be specified using the epilog= argument to ArgumentParser:
"""
parser = argparse.ArgumentParser(
    description='A foo that bars',
    epilog="And that's how you'd foo a bar")
parser.print_help()
"""
usage: argparse.py [-h]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar # <-- here
"""
# parents
"""
Sometimes, several parsers share a common set of arguments. 
Rather than repeating the definitions of these arguments, 
a single parser with all the shared arguments and passed to parents= argument to ArgumentParser can be used. 
The parents= argument takes a list of ArgumentParser objects, collects all the positional and 
optional actions from them, and adds these actions to the ArgumentParser object being constructed:
"""

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent', '2', 'XXX'])
# Namespace(foo='XXX', parent=2)

bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--bar', 'YYY'])
# Namespace(bar='YYY', parent=None)

