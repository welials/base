import argparse

"""
class argparse.BooleanOptionalAction
A subclass of Action for handling boolean flags with positive and negative options. 
Adding a single argument such as --foo automatically creates both --foo and --no-foo options, storing True and False respectively:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
print(parser.parse_args(['--no-foo']))
"""
Namespace(foo=False)
"""
