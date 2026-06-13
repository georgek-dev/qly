# parse.py - parse a file
# Licensed under the Apache-2.0 or BSD 3-Clause license

from qly.output.colors import Colors
import sys

commands = ["val", "ln"]
ra = [4, 2] 
types = ["int", "bool"]
vars = []
var_content = []

def langparse(line):
    global commands, ra, types, vars, var_content
    split = line.split()
    sl = len(split)
    if sl == 0: 
        return
    if split[0] not in commands:
        print(f"{Colors.RED}error E001: {Colors.RESET}command {split[0]} not found")
        sys.exit(1)
    # now run the command depending on what the line is
    for c in commands:
        if split[0] == c:
            i = commands.index(c)
            a = ra[i]
            # we need to check for the required  args length
            if sl != a:
                print(f"{Colors.RED}error E002: {Colors.RESET}{c} takes {a} arguments but {sl} were given")
                sys.exit(0)
            if c == "val":
                if split[1][0] != ".":
                    print(f"{Colors.RED}error E003: {Colors.RESET} variable name {split[1]} does not begin with a .")
                    sys.exit(1)
                if split[2] not in types:
                    print(f"{Colors.RED}error E004: {Colors.RESET}type {split[2]} for a variable is not valid")
                    sys.exit(1)
                if split[2] == "int" and not split[2].isdigit():
                    print(f"{Colors.RED}error E004: {Colors.RESET}type {split[2]} for a variable is not valid")
                if not any(char.isdigit() for char in split[3]) and (split[2] != "bool" or split[3] in ("true", "false")):
                    print(f"{Colors.RED}error E005: {Colors.RESET}{split[3]} is not a valid value for type {split[2]}")
                    sys.exit(1)
                if split[2] == "bool" and (split[3] not in ("true", "false")):
                    print(f"{Colors.RED}error E005: {Colors.RESET}{split[3]} is not a valid value for type {split[2]}")
                    sys.exit(1)
                vars.append(split[1])
                var_content.append(split[3])
            elif c == "ln":
                if split[1][0] != ".":
                    print(f"{Colors.RED}error E003: {Colors.RESET} variable name {split[1]} does not begin with a .")
                    sys.exit(1)
                if split[1] not in vars:
                    print(f"{Colors.RED}error E006: {Colors.RESET} variable {split[1]} doesn't exist")
                    sys.exit(1)
                ti = vars.index(split[1])
                content = var_content[ti]
                print(str(content))
            else:
                print(f"{Colors.RED}error E001: {Colors.RESET}command {split[0]} not found")
                sys.exit(1)
