#!/usr/bin/env python3
first = True
for digit_1 in range(0, 9):
    digit_2 = digit_1 + 1
    while (digit_2 <= 9):
        if (first is True):
            print(f'{digit_1}{digit_2}', end='')
            first = False
        else:
            print(f', {digit_1}{digit_2}', end='')
        digit_2 += 1
print('')
# Print all unique combinations of two different digits from 0 to 9.
# Rules:
#    Digits must be different.
#    Combinations must be printed in ascending order.
#      (Print only the smallest combination of two digits)
#    Format: 01, 02, 03, ..., 89
#      (Numbers must be separated by , followed by a space)
#    No repetition ("01" and "10" are the same combination of digits).
#    You can only use no more than 3 print functions with string format
#    You can only use no more than 2 loops in your code
