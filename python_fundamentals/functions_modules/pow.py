#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    total = 1
    op = 0
    while (op < abs(b)):
        if (b > 0):
            total *= a
        else:
            total /= a
        op += 1
    return total
