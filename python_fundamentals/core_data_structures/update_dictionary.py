#!/usr/bin/env python3
def update_dictionary(a_dictionary, key, value):
    # USELESS: assignment already overwrites or creates.
    # if key in a_dictionary:
    #    a_dictionary[key] = value
    # OVERKILL for a single (re)assignment
    # a_dictionary.update({key: value})
    a_dictionary[key] = value
    return a_dictionary
# If key already exists, replace its value.
# If key does not exist, create it.
# Return the (updated) dictionary.
