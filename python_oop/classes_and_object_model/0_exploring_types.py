#!/usr/bin/env python3

# Exploring types
print("=== Defining basic variables: integer, string, list ===")
number = 42
text = "hello"
numbers = [1, 2, 3]

print("=== Printing their type ===")
print(f"Type of number is {type(number)}")
print(f"Type of text is {type(text)}")
print(f"Type of numbers is {type(numbers)}")


print("=== Printing their id ===")
print(f"Id of number is {id(number)}")
print(f"Id of text is {id(text)}")
print(f"Id of numbers is {id(numbers)}")
print("=== Checking new instance of number ===")

print(f"Id of number is still   {id(number)}")
another_number = 42
print(f"Id of another number is {id(another_number)}")
print("Id is the same because it was the same literal pointed by both vars")
third_number = 41
print(f"Id of third number is   {id(third_number)}")
print("Id is different because different value")
print("  requiring a new literal with new space in memory")

print("=== Trying out calling 'object methods' ===")
print("Picking text variable as an example")
print("dir is available on all objects and list all methods")
print(dir(text))
print(text.upper())
print(text.replace("h", "H"))

print("=== Seeing with examples that instances are different in memory ===")
print("Using new lists with same content as an example")
list_a = [1, 2]
list_b = [1, 2]
print(f"List A has id {id(list_a)}")
print(f"List B has id {id(list_b)}")
