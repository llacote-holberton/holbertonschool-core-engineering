#!/usr/bin/env python3
"""Module defining a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class which will serve
        to hold many common properties and methods
        for various geometry forms"""
    def __init__(self):
        pass

    def area(self):
        raise Exception(f"area() is not implemented")

    def integer_validator(self, name, value):
        if not (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
