import argparse
"""
'help' - This prints a complete help message for all the options in the current parser and then exits. 
By default a help action is automatically added to the parser. See ArgumentParser for details of how the output is created.
"""
"""
'version' - This expects a version= keyword argument in the add_argument() call, and prints version information and exits when invoked:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
print(parser.parse_args(['--version']))
"""
PROG 2.0
"""