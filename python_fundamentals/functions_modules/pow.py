#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    total = 1
    op = 0
    while (op < abs(b)):
        total *= a
        op += 1
    if (b < 0):
        total = 1 / total
    return total
