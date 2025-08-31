import argparse
"""
The base name of sys.argv[0] if a file was passed as argument.

The Python interpreter name followed by sys.argv[0] if a directory or a zipfile was passed as argument.

The Python interpreter name followed by -m followed by the module or package name if the -m option was used.

This default is almost always desirable because it will make the help messages match the string that was used to invoke the program on the command line. However, to change this default behavior, another value can be supplied using the prog= argument to ArgumentParser:
"""
# prog
parser = argparse.ArgumentParser(prog='myprogram')

parser.print_help()
"""
usage: myprogram [-h]
options:
 -h, --help  show this help message and exit
Note that the program name, whether determined from sys.argv[0] or from the prog= argument, is available to help messages using the %(prog)s format specifier.
"""