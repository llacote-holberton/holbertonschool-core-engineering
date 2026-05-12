#!/usr/bin/env python3
"""Module illustrating multiple inheritance to create mixin features"""


class SwimMixin:
    """Swim feature."""

    def swim(self):
        """Informs that creature can swim"""
        print("The creature swims!")


class FlyMixin:
    """Fly feature."""

    def fly(self):
        """Informs that creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Powerful creature."""

    def roar(self):
        """Informs that creature can roar."""
        print("The dragon roars!")


if __name__ == "__main__":
    myDragon = Dragon()
    myDragon.swim()
    myDragon.fly()
    myDragon.roar
