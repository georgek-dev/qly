# ln.py - print a line to the screen
# Licensed under the Apache-2.0 or BSD 3-Clause license

from qly.vars import vars, var_content
from qly.output.errors import error


def ln(split):
    if split[1][0] != ".":
        error("e003", split[1])
    if split[1] not in vars:
        error("e006", split[1])
    ti = vars.index(split[1])
    content = var_content[ti]
    print(str(content))
