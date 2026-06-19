# parse.py - parse a file
# Licensed under the Apache-2.0 or BSD 3-Clause license

from qly.output.colors import Colors
from qly.output.errors import error
from qly.vars import commands, ra, types, vars, var_content, modifiers
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
                # perform exhaustive checks for each variable-type
                if split[2] != "str" and sl != 4:
                    error("e002", c, a, sl)
                if split[1][0] != ".":
                    error("e003", split[1])
                if split[2] not in types:
                    error("e004", split[2])
                if split[2] == "int" and not split[3].isdigit():
                    error("e004", split[2])
                if split[2] == "int":
                    if not any(char.isdigit() for char in split[3]):
                        error("e005", split[3], split[2])
                if split[2] == "str":
                    if not split[3].startswith('"') or split[len(split) - 1].startswith(
                        '"'
                    ):
                        error("e009")
                    if line.count('"') != 2:
                        error("e010")
                if split[2] == "bool" and (split[3] not in ("true", "false")):
                    error("e005", split[3], split[2])
                if split[1] in vars:
                    error("e007", split[1])
                vars.append(split[1])
                if split[2] != "str":
                    var_content.append(split[3])
                    return
                else:
                    text = " ".join(split[3:]).replace('"', "")
                    var_content.append(text)
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
