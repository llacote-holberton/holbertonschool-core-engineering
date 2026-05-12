#!/usr/bin/env python3

#Parent class
class Animal:
    def speak(self):
        return "Some sound"

# First child class
class Dog(Animal):
    pass

# Second child class
class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
