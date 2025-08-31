import argparse
# conflict_handler

parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
parser.print_help()
"""
usage: PROG [-h] [-f FOO] [--foo FOO]

options:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
Note that ArgumentParser objects only remove an action if all of its option strings are overridden. 
So, in the example above, the old -f/--foo action is retained as the -f action, because only the --foo option string was overridden.
"""