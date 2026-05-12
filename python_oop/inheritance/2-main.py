#!/usr/bin/env python3
Rectangle = __import__('1-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r3 = Rectangle(0, 4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
