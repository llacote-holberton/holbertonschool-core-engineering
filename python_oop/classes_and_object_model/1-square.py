#!/usr/bin/env python3
"""Module defining a Square class"""


class Square:
    """Square class with parameterized size
       and basic maths methods like area"""
    def __init__(self, size):
        # _varname means an explicit, fixed name
        #    but for a private member
        # __varname will be computed by Python at runtime
        #   with the concept of name mangling which will
        #   ensure that the property has a unique name
        #   even when being inherited by a subclass
        self.__size = size
