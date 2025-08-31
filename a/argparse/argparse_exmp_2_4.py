import argparse



# description
"""
Most calls to the ArgumentParser constructor will use the description= keyword argument. 
This argument gives a brief description of what the program does and how it works. In help messages, 
the description is displayed between the command-line usage string and the help messages for the various arguments.

By default, the description will be line-wrapped so that it fits within the given space. To change this behavior, see the formatter_class argument.
"""
# epilog
"""
Some programs like to display additional description of the program after the description of the arguments.
Such text can be specified using the epilog= argument to ArgumentParser:
"""
parser = argparse.ArgumentParser(
    description='A foo that bars',
    epilog="And that's how you'd foo a bar")
parser.print_help()
"""
usage: argparse.py [-h]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar # <-- here
"""