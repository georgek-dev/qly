# func_if.py - code for &if 
# SPDX-License-Identifier: Apache-2.0 OR BSD-3-Clause

import qly.vars
from qly.vars import vars, var_content, compare, var_types
from qly.output.errors import error

def func_if(line: str):
    split = line.split(" ")
    obj1 = split[1]
    obj2 = split[3]
    comparison = split[2]
    if comparison not in compare:
        error("e015", comparison)
    if not obj1.startswith("."):
        error("e003", obj1)
    if not obj2.startswith("."):
        error("e003", obj2)
    if obj1 not in vars:
        error("e006", obj1)
    if obj2 not in vars:
        error("e006", obj1)
    index1 = vars.index(obj1)
    index2 = vars.index(obj2)
    content1 = var_content[index1]
    content2 = var_content[index2]
    type1 = var_types[index1]
    type2 = var_types[index2]
    if type1 != type2:
        error("e016", obj1, obj2)
    if type1 == "str" and type2 == "str":
        if str(content1) == str(content2):
            qly.vars.inif = True
    elif type1 == "int" and type2 == "int":
        if int(content1) == int(content2):
            qly.vars.inif = True
    elif type1 == "bool" and type2 == "bool":
        if bool(str(content1).title()) == bool(str(content2).title()):
            qly.vars.inif = True
    else:
        error("e017")