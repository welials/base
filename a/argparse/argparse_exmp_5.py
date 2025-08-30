# prefix_chars
import argparse, sys
"""
Most command-line options will use - as the prefix, e.g. -f/--foo. Parsers that need to support different or additional prefix characters, e.g. for options like +f or /foo, may specify them using the prefix_chars= argument to the ArgumentParser constructor:
"""
parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
parser.parse_args('+f X ++bar Y'.split())
"""
Namespace(bar='Y', f='X')
"""

"""
The prefix_chars= argument defaults to '-'. Supplying a set of characters that does not include - will cause -f/--foo options to be disallowed.
"""

# fromfile_prefix_chars
"""
Sometimes, when dealing with a particularly long argument list, it may make sense to keep the list of arguments 
in a file rather than typing it out at the command line. 
If the fromfile_prefix_chars= argument is given to the ArgumentParser constructor, 
then arguments that start with any of the specified characters will be treated as files, 
and will be replaced by the arguments they contain. For example:
"""
with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
    fp.write('-f\nbar')

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
parser.parse_args(['-f', 'foo', '@args.txt'])
"""
Namespace(f='bar')
"""
"""
Arguments read from a file must be one per line by default (but see also convert_arg_line_to_args()) 
and are treated as if they were in the same place as the original file referencing argument on the command line. 
So in the example above, the expression ['-f', 'foo', '@args.txt'] is considered equivalent to the expression ['-f', 'foo', '-f', 'bar'].
"""

# argument_default
"""
Generally, argument defaults are specified either by passing a default to add_argument() 
or by calling the set_defaults() methods with a specific set of name-value pairs. 
Sometimes however, it may be useful to specify a single parser-wide default for arguments. 
This can be accomplished by passing the argument_default= keyword argument to ArgumentParser. 
For example, to globally suppress attribute creation on parse_args() calls, we supply argument_default=SUPPRESS:
"""
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
parser.parse_args(['--foo', '1', 'BAR'])
"""
Namespace(bar='BAR', foo='1')
"""
parser.parse_args([])
"""
Namespace()
"""
# allow_abbrev
"""
Normally, when you pass an argument list to the parse_args() method of an ArgumentParser, it recognizes abbreviations of long options.

This feature can be disabled by setting allow_abbrev to False:
"""

parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser.add_argument('--foobar', action='store_true')
parser.add_argument('--foonley', action='store_false')
parser.parse_args(['--foon'])
"""
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon
"""