# init.py - entry point for the qly Cli
# Licensed under the Apache 2.0 or BSD 3-Clause license

from qly.file.delegate.stream import parse
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    file = args.file
    parse(file)

# ignore if not running interactively
if __name__ == "__main__":
    main()
