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

print("=== Constraints requirements tests ===")
print("--- Circle with non-int provided ---")
try:
    zero_circle = Circle("radius")
except Exception as e:
    print(e)


print("--- Circle with 0 radius ---")
try:
    zero_circle = Circle(radius=0)
except Exception as e:
    print(e)

print("--- Rectangle with 0 in a dimension (so a line) ---")
try:
    zero_rectangle = Rectangle(width=0, height=10)
except Exception as e:
    print(e)

print("--- Circle with negative dimension ---")
try:
    negative_circle = Circle(-666)
except Exception as e:
    print(e)

print("--- Rectangle with negative in a dimension ---")
try:
    negative_rectangle = Rectangle(width=666, height=-666)
except Exception as e:
    print(e)
