#!/usr/bin/env python3
"""Module defining a Rectangle class"""


class Rectangle:
    """Rectangle class with parameterized size
       and basic maths methods like area and perimeter"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if (self.check_valid_dimension(value, "width")):
            self.__width = value

    @height.setter
    def height(self, value):
        if (self.check_valid_dimension(value, "height")):
            self.__height = value

    def check_valid_dimension(self, value, name="dimension"):
        if not (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
            return False
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")
            return False
        else:
            return True
