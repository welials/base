import argparse

"""
MetavarTypeHelpFormatterиспользует имя аргумента типа для каждого аргумента в качестве отображаемого имени его значений
 (вместо использования dest , как это делает обычный форматировщик):
"""

parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)
parser.print_help()
"""
usage: PROG [-h] [--foo int] float

positional arguments:
  float

options:
  -h, --help  show this help message and exit
  --foo int
"""