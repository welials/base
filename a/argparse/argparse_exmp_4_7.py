import argparse
# exit_on_error
"""
Normally, when you pass an invalid argument list to the parse_args() method of an ArgumentParser, 
it will print a message to sys.stderr and exit with a status code of 2.
If the user would like to catch errors manually, 
the feature can be enabled by setting exit_on_error to False:
"""
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument('--integers', type=int)
parser.print_help()
# _StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
print("#"*100)
try:
    parser.parse_args('--integers a'.split())
except argparse.ArgumentError:
    print('Catching an argumentError')
"""
Catching an argumentError
"""