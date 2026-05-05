#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    if (idx >= 0 and idx < len(my_list)):
        my_list[idx] = element
    return my_list
# If idx is negative or out of range, return the original list unchanged.
# Otherwise, replace the element at position idx with element
#   and return the list.
