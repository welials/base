import argparse

"""
class argparse.BooleanOptionalAction
A subclass of Action for handling boolean flags with positive and negative options. 
Adding a single argument such as --foo automatically creates both --foo and --no-foo options, storing True and False respectively:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
print(parser.parse_args(['--no-foo']))
"""
Namespace(foo=False)
"""
"""
Option value syntax
The parse_args() method supports several ways of specifying the value of an option (if it takes one). In the simplest case, the option and its value are passed as two separate arguments:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')
parser.add_argument('--foo')
parser.parse_args(['-x', 'X'])
"""
Namespace(foo=None, x='X')
"""
print(parser.parse_args(['--foo', 'FOO']))
"""
Namespace(foo='FOO', x=None)
For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument, using = to separate them:
"""
print(parser.parse_args(['--foo=FOO']))
"""
Namespace(foo='FOO', x=None)
For short options (options only one character long), the option and its value can be concatenated:
"""
print(parser.parse_args(['-xX']))
"""
Namespace(foo=None, x='X')
Several short options can be joined together, using only a single - prefix, as long as only the last option (or none of them) requires a value:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', action='store_true')
parser.add_argument('-y', action='store_true')
parser.add_argument('-z')
print(parser.parse_args(['-xyzZ']))
"""
Namespace(x=True, y=True, z='Z')
"""

