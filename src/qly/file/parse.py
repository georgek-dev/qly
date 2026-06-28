# parse.py - parse a file
# SPDX-License-Identifier: Apache-2.0 OR BSD-3-Clause

from qly.output.errors import error
from qly.vars import commands, ra, modifiers, obj, indent
from qly.functions.val import val
from qly.functions.ln import ln
from qly.functions.conditions.obj import startobj

import sys


def langparse(line):
    split = line.split()
    sl = len(split)
    if sl == 0:
        return
    if split[0] not in commands and split[0] not in modifiers and split[0][0] != indent:
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
            elif split[0][0] in obj or split[0][0] == indent:
                break
            else:
                error("e001")

    if split[0][0] == indent:
        # PLEASE don't use if at the moment - still kinda (well alot) broken.
        raise NotImplementedError("if is still being worked on")
    if split[0][0] in obj:
        startobj(line)
