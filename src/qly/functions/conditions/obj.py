# obj.py - handle & lines
# SPDX-License-Identifier: Apache-2.0 OR BSD-3-Clause

import qly.vars
from qly.output.errors import error
from qly.functions.conditions.func_if import func_if


def startobj(line: str):
    split = line.split(" ")
    if split[0][0] != "&":
        error("e014")
    modifier = split[0].split("&")
    if modifier[1] == "if":
        func_if()
    if modifier[1] == "end":
        if qly.vars.inif:
            qly.vars.inif = False
        else:
            error("e018")
    else:
        error("e013", line)
