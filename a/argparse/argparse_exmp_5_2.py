import argparse
"""
'store' - This just stores the argument’s value. This is the default action.

'store_const' - This stores the value specified by the const keyword argument; 
note that the const keyword argument defaults to None. 
The 'store_const' action is most commonly used with optional arguments that specify some sort of flag. For example:
"""

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)
print(parser.parse_args(['--foo']))
parser.print_help()
"""
Namespace(foo=42)
"""