import argparse
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')


"""
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)¶
Create a new ArgumentParser object. All parameters should be passed as keyword arguments. Each parameter has its own more detailed description below, but in short they are:

prog - The name of the program (default: os.path.basename(sys.argv[0]))

usage - The string describing the program usage (default: generated from arguments added to parser)

description - Text to display before the argument help (by default, no text)

epilog - Text to display after the argument help (by default, no text)

parents - A list of ArgumentParser objects whose arguments should also be included

formatter_class - A class for customizing the help output

prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)

fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)

argument_default - The global default value for arguments (default: None)

conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)

add_help - Add a -h/--help option to the parser (default: True)

allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)

exit_on_error - Determines whether or not ArgumentParser exits with error info when an error occurs. (default: True)
"""