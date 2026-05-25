#!/usr/bin/env python3
"""Simple example of file read in Python"""


def write_file(filename="", text=""):
    """Writes file with provided path and content, does not handle problems"""

    count__chars_to_write = len(text)
    count__chars_written = 0
    # print(f"@dev: text to print is {count__chars_to_write}")
    # Using r+ instead of w to be able to read what was just written to check.
    # Actually NO: must use 'w' for "automatic creation of file if not exist"
    # Otherwise I'd need a first block "check if file exist or create it"
    #   THEN ONLY opening it with 'r+' for readwrite mode.
    with open(filename, 'w', encoding="utf-8") as f:
        # Approach "EAFP" (Easier to Ask Forgiveness than Permission)
        #   rather than LBYL (Look Before You Leap)
        try:
            count__chars_written = f.write(text)
            # print(f"@dev chars actually written: {count__chars_written}")
        except OSError as e:
            print(e)
    return count__chars_written
