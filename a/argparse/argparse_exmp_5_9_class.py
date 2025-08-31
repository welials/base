import argparse
"""
The recommended way to create a custom action is to extend Action, 
overriding the __call__() method and optionally the __init__() and format_usage() methods. 
You can also register custom actions using the register() 
method and reference them by their registered name.
An example of a custom action:
"""
class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=FooAction)
parser.add_argument('bar', action=FooAction)
args = parser.parse_args('1 --foo 2'.split())
print(args)
"""
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
"""
print("#"*100)
print(args)
"""
Namespace(bar='1', foo='2')
"""