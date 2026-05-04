#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

last_digit = number % 10
msg_common_part = "Last digit of {} is {}".format(number, last_digit)

if (last_digit > 5):
    print(f'{msg_common_part} and is greater than 5')
elif (last_digit == 0):
    print(f'{msg_common_part} and is zero')
else:
    print(f'{msg_common_part} and is less than 6 and not 0')
