import argparse

parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', help='foo of the %(prog)s program')
parser.print_help()
"""
usage: myprogram [-h] [--foo FOO]  <-- here myprogram

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
"""
