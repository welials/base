import argparse
# Invalid arguments
"""
While parsing the command line, parse_args() checks for a variety of errors, including ambiguous options, invalid types, invalid options, wrong number of positional arguments, etc. When it encounters such an error, it exits and prints the error along with a usage message:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', type=int)
parser.add_argument('bar', nargs='?')

# invalid type
parser.parse_args(['--foo', 'spam'])
"""
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'
"""
# invalid option
parser.parse_args(['--bar'])
"""
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar
"""

# wrong number of arguments
parser.parse_args(['spam', 'badger'])
"""
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger
"""
хлам, [03.09.2025 10:34]
# Arguments containing -
"""
The parse_args() method attempts to give errors whenever the user has clearly made a mistake, but some situations are inherently ambiguous. For example, the command-line argument -1 could either be an attempt to specify an option or an attempt to provide a positional argument. The parse_args() method is cautious here: positional arguments may only begin with - if they look like negative numbers and there are no options in the parser that look like negative numbers:
"""

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')
parser.add_argument('foo', nargs='?')

# no negative number options, so -1 is a positional argument
parser.parse_args(['-x', '-1'])
"""
Namespace(foo=None, x='-1')
"""

# no negative number options, so -1 and -5 are positional arguments
parser.parse_args(['-x', '-1', '-5'])
"""
Namespace(foo='-5', x='-1')
"""

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-1', dest='one')
parser.add_argument('foo', nargs='?')

# negative number options present, so -1 is an option

parser.parse_args(['-1', 'X'])
"""
Namespace(foo=None, one='X')
"""
# negative number options present, so -2 is an option
parser.parse_args(['-2'])
"""
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2
"""
# negative number options present, so both -1s are options
parser.parse_args(['-1', '-1'])
"""
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument
"""
"""
If you have positional arguments that must begin with - and don’t look like negative numbers, you can insert the pseudo-argument '--' which tells parse_args() that everything after that is a positional argument:
"""
parser.parse_args(['--', '-f'])
"""
Namespace(foo='-f', one=None)
"""

хлам, [03.09.2025 10:45]
# Argument abbreviations (prefix matching)
"""
The parse_args() method by default allows long options to be abbreviated to a prefix, if the abbreviation is unambiguous (the prefix matches a unique option):
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-bacon')
parser.add_argument('-badger')
parser.parse_args('-bac MMM'.split())
"""
Namespace(bacon='MMM', badger=None)
"""
parser.parse_args('-bad WOOD'.split())
"""
Namespace(bacon=None, badger='WOOD')
"""
parser.parse_args('-ba BA'.split())
"""
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon
"""
"""
An error is produced for arguments that could produce more than one options. This feature can be disabled by setting allow_abbrev to False.
"""

хлам, [03.09.2025 10:51]
# Beyond sys.argv
"""
Sometimes it may be useful to have an ArgumentParser parse arguments other than those of sys.argv. This can be accomplished by passing a list of strings to parse_args(). This is useful for testing at the interactive prompt:
"""
parser = argparse.ArgumentParser()
parser.add_argument(
    'integers', metavar='int', type=int, choices=range(10),
    nargs='+', help='an integer in the range 0..9')
parser.add_argument(
    '--sum', dest='accumulate', action='store_const', const=sum,
    default=max, help='sum the integers (default: find the max)')
parser.parse_args(['1', '2', '3', '4'])
"""
Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
"""
parser.parse_args(['1', '2', '3', '4', '--sum'])
"""
Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])
"""

хлам, [03.09.2025 10:56]

# The Namespace object
"""
class argparse.Namespace
Simple class used by default by parse_args() to create an object holding attributes and return it.

This class is deliberately simple, just an object subclass with a readable string representation. If you prefer to have dict-like view of the attributes, you can use the standard Python idiom, vars():
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args = parser.parse_args(['--foo', 'BAR'])
vars(args)
"""
{'foo': 'BAR'}
"""
"""
It may also be useful to have an ArgumentParser assign attributes to an already existing object, rather than a new Namespace object. This can be achieved by specifying the namespace= keyword argument:
"""
class C:
    pass

c = C()
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.parse_args(args=['--foo', 'BAR'], namespace=c)
c.foo
"""
'BAR'
"""