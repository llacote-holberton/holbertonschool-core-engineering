#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Module defining Animals example of interfaces"""


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# GOALS
# Create an abstract class named Animal using the ABC package.
#   This class must have an abstract method called sound.
# Create two subclasses of Animal: Dog and Cat.
# Implement the sound method in Dog so it returns the string "Bark".
# Implement the sound method in Cat so it returns the string "Meow".
