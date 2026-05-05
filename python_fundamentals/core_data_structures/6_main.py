#!/usr/bin/env python3
update_dictionary = __import__('update_dictionary').update_dictionary

d = {'language': 'C', 'number': 89, 'track': 'Low level'}
print(update_dictionary(d, 'language', 'Python'))
print(update_dictionary(d, 'city', 'San Francisco'))
