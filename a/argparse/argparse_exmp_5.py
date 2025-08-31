"""
The add_argument() method¶
ArgumentParser.add_argument(name or flags..., *[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest][, deprecated])
Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

name or flags - Either a name or a list of option strings, e.g. 'foo' or '-f', '--foo'.

action - The basic type of action to be taken when this argument is encountered at the command line.

nargs - The number of command-line arguments that should be consumed.

const - A constant value required by some action and nargs selections.

default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.

type - The type to which the command-line argument should be converted.

choices - A sequence of the allowable values for the argument.

required - Whether or not the command-line option may be omitted (optionals only).

help - A brief description of what the argument does.

metavar - A name for the argument in usage messages.

dest - The name of the attribute to be added to the object returned by parse_args().

deprecated - Whether or not use of the argument is deprecated.

The following sections describe how each of these are used.
"""