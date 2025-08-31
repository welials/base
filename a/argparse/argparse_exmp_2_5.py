import argparse


# parents
"""
Sometimes, several parsers share a common set of arguments. 
Rather than repeating the definitions of these arguments, 
a single parser with all the shared arguments and passed to parents= argument to ArgumentParser can be used. 
The parents= argument takes a list of ArgumentParser objects, collects all the positional and 
optional actions from them, and adds these actions to the ArgumentParser object being constructed:
"""

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent', '2', 'XXX'])
foo_parser.print_help()
# Namespace(foo='XXX', parent=2)
print("#"*100)
bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--bar', 'YYY'])
bar_parser.print_help()
# Namespace(bar='YYY', parent=None)
