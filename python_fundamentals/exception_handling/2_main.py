#!/usr/bin/env python3
# Had to rename to keep pycodestyle happy
sp_intlist = __import__('safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = sp_intlist(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = sp_intlist(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = sp_intlist(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

complex_list = [
    1, -666, 77.33, "My_text", ['a', 'b', 'c'],
    {"name": "MyDict", "content": "nothing yet"},
    None, True, "End", False
]
complex_print = sp_intlist(complex_list, 20)
print("Complex list prints: {:d}".format(complex_print))
