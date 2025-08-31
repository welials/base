import argparse
# argument_default
"""
Generally, argument defaults are specified either by passing a default to add_argument() 
or by calling the set_defaults() methods with a specific set of name-value pairs. 
Sometimes however, it may be useful to specify a single parser-wide default for arguments. 
This can be accomplished by passing the argument_default= keyword argument to ArgumentParser. 
For example, to globally suppress attribute creation on parse_args() calls, we supply argument_default=SUPPRESS:
"""
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
print(parser.parse_args(['--foo', '1', 'BAR']))
parser.print_help()
"""
Namespace(bar='BAR', foo='1')
"""
print(parser.parse_args([]))
"""
Namespace()
"""