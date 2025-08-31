import argparse
# conflict_handler
"""
ArgumentParser objects do not allow two actions with the same option string. By default, 
ArgumentParser objects raise an exception if an attempt is made to create an argument with an option string that is already in use:
"""
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
"""
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
Sometimes (e.g. when using parents) it may be useful to simply override any older arguments with the same option string. To get this behavior, the value 'resolve' can be supplied to the conflict_handler= argument of ArgumentParser:
"""
