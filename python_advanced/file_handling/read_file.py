#!/usr/bin/env python3
"""Simple example of file read in Python"""


def read_file(filename=""):
    """Reads file with provided path, assumes it exists and is readable"""
    # 'with' ensures that file is closed automatically even if exception arises
    # 2st param is path, 2nd is "mode" (optional, r default), 3rd is encoding.
    with open(filename, 'r', encoding="utf-8") as f:
        # text = f.read()
        # return text
        print(f.read(), end="")
