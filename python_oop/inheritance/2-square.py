#!/usr/bin/env python3
"""Module defining a Rectangle class"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class = rectangle with equal width & height."""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
