# parse.py - parse a file
# Licensed under the Apache-2.0 or BSD 3-Clause license

from qly.output.colors import Colors
from qly.output.errors import error
from qly.vars import commands, ra, types, vars, var_content
import sys

def langparse(line):
    split = line.split()
    sl = len(split)
    if sl == 0: 
        return
    if split[0] not in commands:
        error("e001", split[0])
    # now run the command depending on what the line is
    for c in commands:
        if split[0] == c:
            i = commands.index(c)
            a = ra[i]
            # we need to check for the required  args length
            if sl != a:
                error("e002", c, a, sl)
            if c == "val":
                # perform exhaustive checks for each variable-type
                if split[1][0] != ".":
                    error("e003", split[1])
                if split[2] not in types:
                    error("e004", split[2])
                if split[2] == "int" and not split[3].isdigit():
                    error("e004", split[2])
                if split[2] == "int":
                    if not any(char.isdigit() for char in split[3]):
                        error("e005", split[3], split[2])
                if split[2] == "bool" and (split[3] not in ("true", "false")):
                    error("e005", split[3], split[2])
                if split[1] in vars:
                    error("e007", split[1])
                vars.append(split[1])
                var_content.append(split[3])
            elif c == "ln":
                if split[1][0] != ".":
                    error("e003", split[1])
                if split[1] not in vars:
                    error("e006", split[1])
                ti = vars.index(split[1])
                content = var_content[ti]
                print(str(content))
            else:
                print(f"{Colors.RED}error E001: {Colors.RESET}command {split[0]} not found")
                sys.exit(1)
