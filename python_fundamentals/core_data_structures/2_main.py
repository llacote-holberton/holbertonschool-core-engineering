#!/usr/bin/env python3
replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 99))
print(replace_in_list(my_list, 15, 99))
print(replace_in_list(my_list, 0, -777))
