import argparse
# default
"""
For optional arguments, the default value is used when the option string was not present at the command line:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
print(parser.parse_args(['--foo', '2']))
"""
Namespace(foo='2')
"""
print(parser.parse_args([]))
"""
Namespace(foo=42)
"""
print("#"*100)
"""
If the target namespace already has an attribute set, the action default will not overwrite it:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
print(parser.parse_args([], namespace=argparse.Namespace(foo=101)))
"""
Namespace(foo=101)
"""
"""
If the default value is a string, the parser parses the value as if it were a command-line argument. In particular, the parser applies any type conversion argument, if provided, before setting the attribute on the Namespace return value. Otherwise, the parser uses the value as is:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--length', default='10', type=int)
parser.add_argument('--width', default=10.5, type=int)
print(parser.parse_args())
"""
Namespace(length=10, width=10.5)
"""
print("#"*100)
"""
If the target namespace already has an attribute set, the action default will not overwrite it:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
print(parser.parse_args([], namespace=argparse.Namespace(foo=101)))
"""
Namespace(foo=101)
"""
print("#"*100)
"""
If the default value is a string, the parser parses the value as if it were a command-line argument. 
In particular, the parser applies any type conversion argument, if provided, 
before setting the attribute on the Namespace return value. Otherwise, the parser uses the value as is:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--length', default='10', type=int)
parser.add_argument('--width', default=10.5, type=int)
print(parser.parse_args())
"""
Namespace(length=10, width=10.5)
"""
print("#"*100)
"""
For positional arguments with nargs equal to ? or *,
 the default value is used when no command-line argument was present:
"""
parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs='?', default=42)
print(parser.parse_args(['a']))
"""
Namespace(foo='a')
"""
print(parser.parse_args([]))
"""
Namespace(foo=42)
"""
print("#"*100)
"""
For required arguments, the default value is ignored. For example, 
this applies to positional arguments with nargs values other than ? or *, or optional arguments marked as required=True.
Providing default=argparse.SUPPRESS causes no attribute to be added if the command-line argument was not present:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=argparse.SUPPRESS)
print(parser.parse_args([]))
"""
Namespace()
"""
print(parser.parse_args(['--foo', '1']))
"""
Namespace(foo='1')
"""