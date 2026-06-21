# parse.py - parse a file
# Licensed under the Apache-2.0 or BSD 3-Clause license
 
from qly.output.errors import error
from qly.vars import commands, ra, modifiers
from qly.functions.val import val
from qly.functions.ln import ln
import sys


def langparse(line):
    split = line.split()
    sl = len(split)
    if sl == 0:
        return
    if split[0] not in commands and split[0] not in modifiers:
        error("e001", split[0])
    # now run the command depending on what the line is
    if split[0] in modifiers:
        if split[len(split) - 1] != split[0]:
            error("e008", split[0])
            sys.exit(1)
        return

    for c in commands:
        if split[0] == c:
            i = commands.index(c)
            a = ra[i]
            # we need to check for the required  args length
            if sl != a and a != "o":
                error("e002", c, a, sl)
            if c == "val":
                val(split, line, c, a)
            elif c == "ln":
                ln(split)
            else:
                error("e001")
