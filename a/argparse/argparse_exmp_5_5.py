import argparse
"""
'append_const' - This stores a list, and appends the value specified by the const keyword argument to the list; 
note that the const keyword argument defaults to None. The 'append_const' action is typically 
useful when multiple arguments need to store constants to the same list. For example:
"""
parser = argparse.ArgumentParser()
parser.add_argument('--str', dest='types', action='append_const', const=str)
parser.add_argument('--int', dest='types', action='append_const', const=int)
print(parser.parse_args('--str --int'.split()))
"""
Namespace(types=[<class 'str'>, <class 'int'>])
"""