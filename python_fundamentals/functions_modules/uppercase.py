#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if (n >= 97 and n < 97+26):
            c = chr(ord(c)-32)
        print(c, end='')
    print('')
# .format()
