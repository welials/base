import argparse
"""
'append' - This stores a list, and appends each argument value to the list. 
It is useful to allow an option to be specified multiple times. 
If the default value is non-empty, the default elements will be present in the parsed value for the option, 
with any values from the command line appended after those default values. Example usage:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
print(parser.parse_args('--foo 1 --foo 2'.split()))
parser.print_help()
"""
Namespace(foo=['1', '2'])
"""