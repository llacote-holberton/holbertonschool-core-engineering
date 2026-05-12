#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Module illustrating multiple inheritance"""


class Fish():
    """Representation of Fishes."""

    def swim(self):
        """Informs that fish can swim"""
        print("The fish is swimming")

    def habitat(self):
        """Informs where fish live"""
        print("The fish lives in water")


class Bird():
    """Representation of Birds."""

    def fly(self):
        """Informs that birds can fly"""
        print("The bird is flying")

    def habitat(self):
        """Informs where birds live"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """Informs that flying fishes can fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """Informs that flying fishes can swmi"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Informs where flying fishes live"""
        print("The flying fish lives both in water and the sky!")

# Construct a FlyingFish class that inherits from
#   both a Fish class and a Bird class.
# Within FlyingFish, override methods from both parents.
# The goal is to understand multiple inheritance and
#   how Python determines method resolution order.
