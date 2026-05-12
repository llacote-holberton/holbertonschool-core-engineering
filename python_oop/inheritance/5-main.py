#!/usr/bin/env python3
Rectangle = __import__('2-rectangle').Rectangle
Square = __import__('2-square').Square

s = Square(13)

print(s)
print(s.area())

shapes = [Rectangle(3, 5), Square(4)]

for shape in shapes:
    print(shape.area())
