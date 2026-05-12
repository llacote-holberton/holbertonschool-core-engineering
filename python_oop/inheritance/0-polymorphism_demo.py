#!/usr/bin/env python3

#Parent class
class Animal:
    def speak(self):
        return "Some sound"

# First child class
class Dog(Animal):
    def speak(self):
        return "Woof"

# Second child class
class Cat(Animal):
    def speak(self):
        return "Meow"

# Step 0 to 4
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

# Step 5
print("---")
animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())
