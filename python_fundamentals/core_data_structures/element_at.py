#!/usr/bin/env python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return None
    return my_list[idx]
# If idx is negative or out of range, return None.
# Otherwise, return the element at position idx.
