#!/usr/bin/env python3
from shapes import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

try:
    # Will work since objects do implement the methods called inside shape_info
    shape_info(circle)
    shape_info(rectangle)
    # Won't work because basic string
    shape_info("A simple string")

except AttributeError as e:
    print(e)
