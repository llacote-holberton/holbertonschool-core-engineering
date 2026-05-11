#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(f"elements: {nb_print}")

complex_list = [
    1, -666, 77.33, "My_text", ['a', 'b', 'c'],
    {"name": "MyDict", "content": "nothing yet"},
    None, True, "End"
]
complex_print = safe_print_list(complex_list, 10)
print(f"Complex list, {complex_print} items were printed for 10 required")
