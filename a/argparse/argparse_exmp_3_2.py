import argparse
import textwrap

"""
Passing RawDescriptionHelpFormatter as formatter_class= indicates that description and epilog are already correctly formatted and should not be line-wrapped:
"""
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it
        '''))
parser.print_help()
"""
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

options:
 -h, --help  show this help message and exit
"""

"""
RawTextHelpFormatterСохраняет пробелы для всех видов справочного текста, включая описания аргументов. 
Однако несколько переносов строк заменяются одним. Если вы хотите сохранить несколько пустых строк, добавьте пробелы между переносами строк.
"""