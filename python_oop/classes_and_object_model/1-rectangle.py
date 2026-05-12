#!/usr/bin/env python3
"""Module defining a Rectangle class"""


class Rectangle:
    """Rectangle class with parameterized size
       and basic maths methods like area and perimeter"""

    def __init__(self, width=0, height=0):
        """"Initialize a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle with validation."""
        if (self.check_valid_dimension(value, "width")):
            self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle with validation."""
        if (self.check_valid_dimension(value, "height")):
            self.__height = value

    def check_valid_dimension(self, value, name="dimension"):
        """Validate if a dimension is a positive integer."""
        if not (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
            return False
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")
            return False
        else:
            return True
