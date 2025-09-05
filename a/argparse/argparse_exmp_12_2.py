import argparse

# Partial parsing
"""
ArgumentParser.parse_known_args(args=None, namespace=None)
Sometimes a script only needs to handle a specific set of command-line arguments, leaving any unrecognized a
rguments for another script or program. In these cases, the parse_known_args() method can be useful.

This method works similarly to parse_args(), but it does not raise an error for extra, unrecognized arguments. 
Instead, it parses the known arguments and returns a two item tuple that contains the populated namespace and the list of any unrecognized arguments.
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')
print(parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam']))
"""
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
"""
# Customizing file parsing
"""
ArgumentParser.convert_arg_line_to_args(arg_line)
Arguments that are read from a file (see the fromfile_prefix_chars keyword argument 
to the ArgumentParser constructor) are read one argument per line. convert_arg_line_to_args() can be overridden for fancier reading.

This method takes a single argument arg_line which is a string read from the argument file. 
It returns a list of arguments parsed from this string. The method is called once per line read from the argument file, in order.

A useful override of this method is one that treats each space-separated word as an argument. 
The following example demonstrates how to do this:
"""

class MyArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        return arg_line.split()

# Exiting methods
"""
ArgumentParser.exit(status=0, message=None)
This method terminates the program, exiting with the specified status and, 
if given, it prints a message to sys.stderr before that. The user can override this method to handle these steps differently:
"""
class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)
"""
ArgumentParser.error(message)
This method prints a usage message, including the message, to sys.stderr and terminates the program with a status code of 2.
"""

# Intermixed parsing
"""
ArgumentParser.parse_intermixed_args(args=None, namespace=None)
ArgumentParser.parse_known_intermixed_args(args=None, namespace=None)
A number of Unix commands allow the user to intermix optional arguments with positional arguments. 
The parse_intermixed_args() and parse_known_intermixed_args() methods support this parsing style.

These parsers do not support all the argparse features, and will raise exceptions 
if unsupported features are used. In particular, subparsers, and mutually exclusive groups that include both optionals and positionals are not supported.

The following example shows the difference between parse_known_args() 
and parse_intermixed_args(): the former returns ['2', '3'] as unparsed arguments, while the latter collects all the positionals into rest.
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('cmd')
parser.add_argument('rest', nargs='*', type=int)
print(parser.parse_known_args('doit 1 --foo bar 2 3'.split()))
"""
(Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
"""
print(parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split()))
"""
Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])
"""
"""
parse_known_intermixed_args() returns a two item tuple containing the populated namespace 
and the list of remaining argument strings. parse_intermixed_args() raises an error if there are any remaining unparsed argument strings.
"""
