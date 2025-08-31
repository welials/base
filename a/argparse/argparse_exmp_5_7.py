import argparse
"""
'count' - This counts the number of times a keyword argument occurs. 
For example, this is useful for increasing verbosity levels:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count', default=0)
print(parser.parse_args(['-vvv']))
"""
Namespace(verbose=3)
"""