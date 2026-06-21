# parse.py - parse a file
# Licensed under the Apache-2.0 or BSD 3-Clause license

from qly.output.colors import Colors
from qly.output.errors import error
from qly.vars import commands, ra, vars, var_content, modifiers
from qly.functions.val import val

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
                if split[1][0] != ".":
                    error("e003", split[1])
                if split[1] not in vars:
                    error("e006", split[1])
                ti = vars.index(split[1])
                content = var_content[ti]
                print(str(content))
            else:
                print(
                    f"{Colors.RED}error E001: {Colors.RESET}command {split[0]} not found"
                )
                sys.exit(1)
