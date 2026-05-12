#!/usr/bin/env python3
"""Module defining a Rectangle class"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class = rectangle with equal width & height."""
    def __init__(self, size):
        self.integer_validator("size", size)
        # WILL NOT work because of the name mangling
        # Or rather would "work" as it would create
        # _Square__width as the real name.
        # AND if we don't re-implement area()
        # if will look for the one in parent class
        # AND because of how we had to write it
        #   it would try to use variables which are
        #   "local to the parent" so "_Rectangle__width" etc.
        # BECAUSE exercice forbids the use of getters/setters
        #   (and therefore also properties) only way is to
        #   use the parent's constructor meaning that the
        #   size will be used to create "Rectangle related" vars.
        # self.__width = size
        # self.__height = size
        # Super returns the "parent factory" (parent class) to
        # so we can use its own constructor for our instance
        # (= use Rectangle factory to create a Square object)
        super().__init__(size, size)
