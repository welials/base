import argparse
# choices
"""
Some command-line arguments should be selected from a restricted set of values. 
These can be handled by passing a sequence object as the choices keyword argument to add_argument(). 
When the command line is parsed, argument values will be checked, 
and an error message will be displayed if the argument was not one of the acceptable values:
"""
parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
print(parser.parse_args(['rock']))
"""
Namespace(move='rock')
"""
print(parser.parse_args(['fire']))
"""
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')
"""