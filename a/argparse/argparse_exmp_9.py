import argparse
# deprecated
"""
During a project’s lifetime, some arguments may need to be removed from the command line. 
Before removing them, you should inform your users that the arguments are deprecated and will be removed. 
The deprecated keyword argument of add_argument(), which defaults to False, 
specifies if the argument is deprecated and will be removed in the future. 
For arguments, if deprecated is True, then a warning will be printed to sys.stderr when the argument is used:
"""
parser = argparse.ArgumentParser(prog='snake.py')
parser.add_argument('--legs', default=0, type=int, deprecated=True)
print(parser.parse_args([]))
"""
Namespace(legs=0)
"""
print(parser.parse_args(['--legs', '4']))
"""
snake.py: warning: option '--legs' is deprecated
Namespace(legs=4)
"""