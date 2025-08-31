import argparse
# nargs
"""
ArgumentParser objects usually associate a single command-line argument with a single action to be taken. 
The nargs keyword argument associates a different number of command-line arguments with a single action. 
See also Specifying ambiguous arguments. The supported values are:
N (an integer). N arguments from the command line will be gathered together into a list. For example:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=2)
parser.add_argument('bar', nargs=1)
print(parser.parse_args('c --foo a b'.split()))
"""
Namespace(bar=['c'], foo=['a', 'b'])
"""