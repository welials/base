import argparse

# Mutual exclusion
"""
ArgumentParser.add_mutually_exclusive_group(required=False)
Create a mutually exclusive group. 
argparse will make sure that only one of the arguments in the mutually exclusive group was present on the command line:
"""
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
parser.parse_args(['--foo'])
"""
Namespace(bar=True, foo=True)
"""
print(parser.parse_args(['--bar']))
"""
Namespace(bar=False, foo=False)
"""
print(parser.parse_args(['--foo', '--bar']))
"""
usage: PROG [-h] [--foo | --bar]
PROG: error: argument --bar: not allowed with argument --foo
"""
"""
The add_mutually_exclusive_group() method also accepts a required argument, 
to indicate that at least one of the mutually exclusive arguments is required:
"""

parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
print(parser.parse_args([]))
"""
usage: PROG [-h] (--foo | --bar)
PROG: error: one of the arguments --foo --bar is required
"""
"""
Note that currently mutually exclusive argument groups do not support the title and
description arguments of add_argument_group(). However, a mutually exclusive group can be added to an 
argument group that has a title and description. For example:
"""
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_argument_group('Group title', 'Group description')
exclusive_group = group.add_mutually_exclusive_group(required=True)
exclusive_group.add_argument('--foo', help='foo help')
exclusive_group.add_argument('--bar', help='bar help')
parser.print_help()
"""
usage: PROG [-h] (--foo FOO | --bar BAR)

options:
  -h, --help  show this help message and exit

Group title:
  Group description

  --foo FOO   foo help
  --bar BAR   bar help
"""
"""
Changed in version 3.11: Calling add_argument_group() or add_mutually_exclusive_group() on a mutually exclusive group is deprecated. 
These features were never supported and do not always work correctly.
The functions exist on the API by accident through inheritance and will be removed in the future.
"""