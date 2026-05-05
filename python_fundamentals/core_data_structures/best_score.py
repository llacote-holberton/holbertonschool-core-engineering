#!/usr/bin/env python3
def best_score(a_dictionary):
    # Dictionaries don't have built-in sort
    # So only way is to get an iterable from it
    # Because we want to return the KEY and not VALUE directly
    #   we cannot just use sort() builtin on "dict.values()"
    # We have to use dict.items to get an iterable made of
    # key/value pairs THEN put it into sort()...
    # AND put the whole as the parameter expression to the dict()
    #   explicit dictionary creation method.

    # DOESN'T WORK as .items() returns a special "view" object,
    #   not an actual list.
    # sorted_by_best = dict((a_dictionary.items).sort(reverse=True) )

    # START WITH GUARD CLAUSES FOR non-dictionary or empty one
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    # if len(a_dictionary) == 1:
    #    return a_dictionary[0]
    else:
        # DOESN'T WORK AND USELESS
        # sorted_by_best = dict(sorted(a_dictionary.items()))
        # return sorted_by_best.pop(0)
        return max(a_dictionary, key=a_dictionary.get)
# Goal: return the key with the biggest integer value.
# You may assume that all values are integers.
# If a_dictionary is None or empty, return None.
# You may assume all values are different.
# Docs: https://docs.python.org/3/library/stdtypes.html#dict
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
