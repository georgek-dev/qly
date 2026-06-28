# errors.py - error-directory of qly interpreter errors
# SPDX-License-Identifier: Apache-2.0 OR BSD-3-Clause

import sys
from qly.output.colors import Colors


def error(e, args1="", args2="", args3=""):
    errors = {
        "e001": "command %s not found" % args1,
        "e002": "%s takes %s arguments but %s were given" % (args1, args2, args3),
        "e003": "variable name %s does not begin with ." % args1,
        "e004": "type %s for a variable is not valid" % args1,
        "e005": "%s is not a valid value for type %s" % (args1, args2),
        "e006": "variable %s doesn't exist" % args1,
        "e007": "variable %s already exists" % args1,
        "e008": "modifier %s not closed" % args1,
        "e009": "started string not closed",
        "e010": "too many occurences of %s" % args1,
        "e011": "\" and ' mismatch",
        "e012": "wrong type of variable passed - please report this",
        "e013": "undefined object %s" % args1,
        "e014": "object does not begin with & - please report this",
        "e015": "comparison %s not found" % args1,
        "e016": "type mismatch between variables %s and %s" % (args1, args2),
        "e017": "error in if function - please report this",
        "e018": "trying to end not started indented block"
    }
    print(
        f"{Colors.RED}error {e.upper()}:{Colors.RESET} {errors.get(e.lower(), 'Unknown error - please report this!')}"
    )
    sys.exit(1)
