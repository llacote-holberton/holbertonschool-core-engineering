#!/usr/bin/env python3
Square = __import__('6-square').Square

print("=== OFFICIAL TESTS ===")
print("--- Square of size 5, offset 0")
my_square = Square(5, (0, 0))
print(my_square)

print("--")
print("--- Square of size 5, offset 4 vertical, 1 horizontal")

my_square = Square(5, (4, 1))
print(my_square)
print("--")

print("=== ADDITIONAL TESTS ===")
print("== Testing my checks on position tuple ==")
try:
    print("Giving string argument, should return False")
    print(my_square.is_position("0,0"))
except TypeError as e:
    print(e)

try:
    print("Giving tuple with negative member, should return False")
    print(my_square.is_position((-1, 10)))
except TypeError as e:
    print(e)

try:
    print("Giving tuple with non-int member, would return False...")
    print(my_square.is_position((777, False)))
    print("  If not for the horrendous implicit conversion of Python")
    print("making the 'False' boolean type value")
    print("converted as int '0' on the fly. -_- -_- -_-.")
    print("Gosh, how can people work with that???")
except TypeError as e:
    print(e)

try:
    print("Giving tuple too many members")
    print(my_square.is_position((6, 66, 666)))
except TypeError as e:
    print(e)

print("== Testing Square edge cases ==")

print("--- Square of size 0, offset 4 vertical, 1 horizontal")
my_square = Square(0, (4, 8))
print("--")

try:
    print("--- Square of size -1, offset 2 vertical, 0 horizontal")
    my_square = Square(-1, (2, 0))
    print("--")
except (ValueError, TypeError) as e:
    print(e)

try:
    print("--- Square of size 7, offset -1 vertical, -1 horizontal")
    my_square = Square(7, (-1, -1))
    print("--")
except (ValueError, TypeError) as e:
    print(e)
