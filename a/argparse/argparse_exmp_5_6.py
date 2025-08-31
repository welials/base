import argparse
"""
'extend' - This stores a list and appends each item from the multi-value argument list to it. 
The 'extend' action is typically used with the nargs keyword argument value '+' or '*'. 
Note that when nargs is None (the default) or '?', 
each character of the argument string will be appended to the list. Example usage:
"""
parser = argparse.ArgumentParser()
parser.add_argument("--foo", action="extend", nargs="+", type=str)
print(parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"]))
"""
Namespace(foo=['f1', 'f2', 'f3', 'f4'])
"""