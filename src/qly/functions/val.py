# val.py - source code for the val function
# Licensed under the Apache-2.0 or BSD 3-Clause

from qly.output.errors import error
from qly.vars import types, vars, var_content


def val(split, line, c, a):
    if type(split) is not list:
        error("e012")
    sl = len(split)
    if split[2] != "str" and sl != 4:
        error("e002", c, a, sl)
    if split[1][0] != ".":
        error("e003", split[1])
    if split[2] not in types:
        error("e004", split[2])
    if split[2] == "int" and not split[3].isdigit():
        error("e004", split[2])
    if split[2] == "int" and not any(char.isdigit() for char in split[3]):
        error("e005", split[3], split[2])
    if split[2] == "str":
        text = " ".join(split[3:])
        if ('"' in line or "'" in line) and (
            line.count('"') != 2 or line.count("'") != 2
        ):
            error("e011")
        if (not text.startswith('"') or not text.endswith('"')) and (
            not text.startswith("'") or not text.endswith("'")
        ):
            error("e009")
        if ('"' in line and line.count('"') != 2) or (
            "'" in line and line.count("'") != 2
        ):
            error("e010", '"' if line.count('"') != 2 else "'")
        if split[2] == "bool" and (split[3] not in ("true", "false")):
            error("e005", split[3], split[2])
        if split[1] in vars:
            error("e007", split[1])
        vars.append(split[1])
    if split[2] != "str":
        var_content.append(split[3])
    else:
        text = " ".join(split[3:]).replace('"', "").replace("'", "")
        var_content.append(text)
