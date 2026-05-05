#!/usr/bin/env python3
def common_elements(set_1, set_2):
    # Ideally we'd sort the sets before comparing.
    # Can we do that? Actually no need, because...
    # a) sets have no duplicate members by definition
    # b) Python provides specific operators for most evaluations.
    return set_1 & set_2
# Goal: return a new set containing only elements present in both sets.
# Doc: https://docs.python.org/3/tutorial/datastructures.html#sets
