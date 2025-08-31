import argparse


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