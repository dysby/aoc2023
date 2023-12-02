#!/usr/bin/env python3

import argparse
import importlib
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Select day to answer")
    parser.add_argument(
        "input",
        default=sys.stdin,
        type=argparse.FileType("r"),
        help="File to read input, default to stdin",
    )
    args = parser.parse_args()

    # Contrived example of generating a module named as a string
    full_module_name = f"answers.day{args.day}"
    # The file gets executed upon import, as expected.
    day_module = importlib.import_module(full_module_name)
    # Then you can use the module like normal
    func = getattr(day_module, "answer")
    func(args.input)


if __name__ == "__main__":
    main()
