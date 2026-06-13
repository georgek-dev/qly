# stream.py - handles the whole file stream process for qly
# licensed under the Apache-2.0 or BSD 3-Clause license

from qly.file.parse import langparse
from qly.output.colors import Colors 
from pathlib import Path
import sys

def parse(file):
    loc = Path(file)
    if not loc.is_file():
        print(f"{Colors.BOLD_RED}error: {Colors.RESET}{Colors.HI_RED}file {loc} doesn't exist{Colors.RESET}")
        if loc.is_dir():
            print(f"{Colors.BOLD_YELLOW}note: {Colors.RESET}{Colors.HI_YELLOW}{loc} is a directory - did you mean a file in it?{Colors.RESET}")
        sys.exit(1)
    with open(loc, "r") as f:
        lines = f.readlines()
    # parse lines to interpret the lines for commands 
    for curr in lines:
        langparse(curr)
