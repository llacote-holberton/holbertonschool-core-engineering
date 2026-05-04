#!/usr/bin/env python3
# Confer documentation on string formatting methods
# https://www.datacamp.com/tutorial/python-string-interpolation

# Basic print
print("Language: Python")

# Basic formatting (can also use positional with 0, 1 etc or names)
version = 3
# WRONG: creates a "data tuple"!!
# version_message = "Version: {}", version
version_message = "Version: {}".format(version)
print(version_message)

# C-like formatting
pi = 3.14159
pi_output = "Pi approx: %.2f" % pi
print(pi_output)

# F-string formatting
print(f'Computation valid: {2*2 == 4}')
