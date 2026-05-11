#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list
safe_print_integer = __import__('safe_print_integer').safe_print_integer

complex_list = [
    1, -666, 77.33, "My_text", ['a', 'b', 'c'],
    {"name": "MyDict", "content": "nothing yet"},
    None, True, "End"
]
complex_print = safe_print_list(complex_list, 10)
print(f"Complex list, {complex_print} items were printed for 10 required")

for i in complex_list:
    print(f"Could print {i} as integer? {safe_print_integer(i)}")
