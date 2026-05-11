#!/usr/bin/env python3
safe_print_division = __import__('safe_print_division').safe_print_division

print("== Basic integers example ==")
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

print("== Forbidden division by zero example ==")
a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

complex_list = [
    1, -666, 77.33, "My_text", ['a', 'b', 'c'],
    {"name": "MyDict", "content": "nothing yet"},
    None, True, "End", False
]
print("== Float example ==")
result = safe_print_division(666.999, 3)
print("666.999 / 3 = {}".format(result))

print("== Negative example ==")
print("72428 / -12 = {}".format(safe_print_division(72428, -12)))

print("== ValueError example ==")
result = safe_print_division("Toto", 3)
print("Toto / 3 = {}".format(result))
