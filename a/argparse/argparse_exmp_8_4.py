import argparse
# help
"""
The help value is a string containing a brief description of the argument. 
When a user requests help (usually by using -h or --help at the command line), 
these help descriptions will be displayed with each argument.
The help strings can include various format specifiers to avoid 
repetition of things like the program name or the argument default. 
The available specifiers include the program name, 
%(prog)s and most keyword arguments to add_argument(), e.g. %(default)s, %(type)s, etc.:
"""
parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('bar', nargs='?', type=int, default=42,
                    help='the bar to %(prog)s (default: %(default)s)')
parser.print_help()
"""
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

options:
 -h, --help  show this help message and exit
"""
"""
As the help string supports %-formatting, if you want a literal % to appear in the help string, you must escape it as %%.

argparse supports silencing the help entry for certain options, by setting the help value to argparse.SUPPRESS:
"""
print("#"*100)

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', help=argparse.SUPPRESS)
parser.print_help()
"""
usage: frobble [-h]

options:
  -h, --help  show this help message and exit
"""