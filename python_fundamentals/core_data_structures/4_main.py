#!/usr/bin/env python3
add_tuple = __import__('add_tuple').add_tuple

print(add_tuple((1, 89), (88, 11)))
print(add_tuple((1, 89), (1, )))
print(add_tuple((1, 89), ()))
print(add_tuple((), ()))
print(add_tuple((-100, 5), (23, -5)))

