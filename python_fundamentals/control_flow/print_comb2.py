#!/usr/bin/env python3
for number in range(0, 99+1):
    if (number < 99):
        print("{0:02d}".format(number), end=", ")
    else:
        print(f'{number:02d}')
# Using +1 as upper bound is NOT included.
# Using different formatted string syntax to remember several exist.
