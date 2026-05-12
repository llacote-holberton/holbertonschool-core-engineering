#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi
"""Module illustrating inheritance with Shapes"""


# WARNING: do NOT forget to inherit from ABC so that
#   this class is actually defined as abstract
class Shape(ABC):
    """Class defining basic asbtract Shape representation"""

    @abstractmethod
    def area(self):
        """Surface area: abstract because depends on each shape"""
        pass

    def perimeter(self):
        """Shape perimeter: abstract because depends on each shape"""
        pass

    def is_positive_integer(self, value):
        """Method checking value is usable to define a shape"""
        return (isinstance(value, int) and value > 0)

    # Message template used when is_positive_integer check has failed.
    msg = "Parameter {name} must be strictly positive integer."


class Circle(Shape):
    """Class defining basic round 2d shape"""

    def __init__(self, radius):
        """Circle constructor"""
        if (self.is_positive_integer(radius)):
            self.__radius = radius
        else:
            raise TypeError(self.msg.format(name="radius"))

    def area(self):
        """Circle area is squared radius multiplied by Pi"""
        # Warning: power symbol is not ^ like in C but **
        return (pi * (self.__radius ** 2))

    def perimeter(self):
        """Circle perimeter is twice radius multiplied by Pi"""
        return (2 * pi * self.__radius)


class Rectangle(Shape):
    """Class defining basic 2d quadrilater"""

    def __init__(self, width, height):
        """Rectangle constructor"""
        if not (self.is_positive_integer(width)):
            raise TypeError(self.msg.format(name="width"))
        elif not (self.is_positive_integer(height)):
            raise TypeError(self.msg.format(name="height"))
        self.__width = width
        self.__height = height

    def area(self):
        """Quadrilater area is multiplying width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Quadrilater perimeter is doubling addition of width and height"""
        return (self.__width + self.__height) * 2


def shape_info(shape: Shape):
    """
    We try to print mathematical informations by calling methods
    without checking any way if the target object actually has them.
    This is stupid, horrible, and the worst ever development practice.
    But apparently this is 'the Python way'.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    try:
        test = Circle(-1)
    except Exception:
        pass

    mytest = Circle(3)
    print("Perimeter: ", mytest.perimeter())
    print("Area: ", mytest.area())
    print(pi)

# GOALS
# Create an abstract class named Shape
#   with two abstract methods: area and perimeter.
# Implement two concrete classes: Circle and Rectangle,
#   both inheriting from Shape.
# Each class must provide implementations for area and perimeter.
# Write a standalone function named shape_info that
#   accepts an object of type Shape by duck typing
#   and prints its area and perimeter.
# Test shape_info with instances of both Circle and Rectangle.
