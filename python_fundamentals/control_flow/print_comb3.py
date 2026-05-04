#!/usr/bin/env python3
first = True
for digit_1 in range(0, 9):
    digit_2 = digit_1 + 1
    while (digit_2 <= 9):
        if (first is True):
            print("{0}{1}".format(digit_1, digit_2), end='')
            first = False
        else:
            print(f', {digit_1}{digit_2}', end='')
        digit_2 += 1
print('')
