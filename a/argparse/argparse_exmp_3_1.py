import argparse
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

parser.print_help()
"""
usage: PROG [-h]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit
likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines
"""