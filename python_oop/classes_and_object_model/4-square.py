#!/usr/bin/env python3
"""Module defining a Square class"""


class Square:
    """Square class with parameterized size
       and basic maths methods like area"""
    def __init__(self, size=0):
        # NOT self.size() because defined as a property.
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if not (size >= 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        side = self.__size
        return side * side
