import argparse
import textwrap
"""
class argparse.RawDescriptionHelpFormatter¶
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
class argparse.MetavarTypeHelpFormatter
RawDescriptionHelpFormatter and RawTextHelpFormatter give more control over how textual descriptions are displayed. 
By default, ArgumentParser objects line-wrap the description and epilog texts in command-line help messages:
"""
parser = argparse.ArgumentParser(
    prog='PROG',
    description='''this description
        was indented weird
            but that is okay''',
    epilog='''
            likewise for this epilog whose whitespace will
        be cleaned up and whose words will be wrapped
        across a couple lines''')
"""
parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit
likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines
"""
#
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

"""
ArgumentDefaultsHelpFormatterавтоматически добавляет информацию о значениях по умолчанию в каждое из сообщений справки аргумента:
"""

parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--foo', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
parser.print_help()
"""
usage: PROG [-h] [--foo FOO] [bar ...]

positional arguments:
 bar         BAR! (default: [1, 2, 3])

options:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)
"""

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