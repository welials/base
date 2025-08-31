import argparse, sys
# fromfile_prefix_chars
"""
Sometimes, when dealing with a particularly long argument list, it may make sense to keep the list of arguments 
in a file rather than typing it out at the command line. 
If the fromfile_prefix_chars= argument is given to the ArgumentParser constructor, 
then arguments that start with any of the specified characters will be treated as files, 
and will be replaced by the arguments they contain. For example:
"""
with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
    fp.write('-f\nbar')

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
print(parser.parse_args(['-f', 'foo', '@args.txt']))
parser.print_help()
"""
Namespace(f='bar')
"""
"""
Arguments read from a file must be one per line by default (but see also convert_arg_line_to_args()) 
and are treated as if they were in the same place as the original file referencing argument on the command line. 
So in the example above, the expression ['-f', 'foo', '@args.txt'] is considered equivalent to the expression ['-f', 'foo', '-f', 'bar'].
"""