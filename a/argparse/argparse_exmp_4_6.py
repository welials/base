import argparse
# add_help
"""
By default, ArgumentParser objects add an option which simply displays the parser’s help message. 
If -h or --help is supplied at the command line, the ArgumentParser help will be printed.
Occasionally, it may be useful to disable the addition of this help option. 
This can be achieved by passing False as the add_help= argument to ArgumentParser:
"""
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parser.add_argument('--foo', help='foo help')
parser.print_help()
"""
usage: PROG [--foo FOO]

options:
 --foo FOO  foo help
"""
"""
The help option is typically -h/--help. 
The exception to this is if the prefix_chars= is specified and does not include -, 
in which case -h and --help are not valid options. In this case, the first character in prefix_chars is used to prefix the help options:
"""
print("#"*100)

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
parser.print_help()
"""
usage: PROG [+h]

options:
  +h, ++help  show this help message and exit
"""