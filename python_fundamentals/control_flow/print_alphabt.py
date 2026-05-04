#!/usr/bin/env python3
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in "eq":
        # Ternary expression is inverted in Python BECAUSE WHY NOT FFS
        print("{}".format(chr(char)), end='\n' if char == ord('z') else '')
