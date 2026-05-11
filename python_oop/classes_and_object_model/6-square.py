#!/usr/bin/env python3
"""Module defining a Square class"""


class Square:
    """Square class with parameterized size
       and basic maths methods like area"""
    def __init__(self, size=0, position=(0, 0)):
        # NOT self.size() because defined as a property.
        self.size = size
        self.position = position

    def __str__(self):
        # Position is used to offset...
        # a means "spaces before start of square lines"
        # b means full lines before starting print.
        # As Python is a crude language with
        #   limited string manipulations methods
        # Only way is to either use concatenation OR
        #   create a list of "substrings" and join them all
        #   in a final one with list method join().
        if (self.size > 0):
            height_offset = "\n" * self.position[1]
            square_line = " " * self.position[0] + "#" * self.size + '\n'
            square = square_line * self.size
            final_string = height_offset + square
        else:
            final_string = '\n'
        return final_string

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (self.is_position(position) is False):
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)
        else:
            self.__position = position

    # Stupid me. I designed all the logic of conditions as
    # "does not fulfill conditions" THEN I re-reverse the intent
    #  in the caller xd
    # def is_position(self, value):
    #     return (
    #         (not isinstance(value, tuple))
    #         or len(value) != 2
    #         or (not (isinstance(value[0], int) and value[0] >=0))
    #         or (not (isinstance(value[1], int) and value[1] >=0))
    #     )
    def is_position(self, value):
        return (
          isinstance(value, tuple)
          and len(value) == 2
          # NOTE: boolean would be automatically converted by Python
          # So False -> 0 would validate the isinstance check.
          # That is horrible, scum practice. But since exercise
          # does NOT require forbidding implicit conversion... -_-
          and isinstance(value[0], int) and value[0] >= 0
          and isinstance(value[1], int) and value[1] >= 0
        )

    def my_print(self):
        print(self)
    # OLD METHOD
    #    if self.size == 0:
    #        print("")
    #    else:
    #        for i in range(0, self.size):
    #            for j in range(0, self.size):
    #                print('#', end="")
    #            print("")
