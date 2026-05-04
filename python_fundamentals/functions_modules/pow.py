#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    total = a
    op = 1
    while (op < b):
        total *= a
        op += 1
    return total
