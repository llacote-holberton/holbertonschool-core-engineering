#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
