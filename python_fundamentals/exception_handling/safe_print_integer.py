#!/usr/bin/env python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    # We need to catch two types of value hence using "tuple syntax"
    # ValueError when given value is of a type which could
    #   theorically be converted (like string "66")
    #   but in context was unusable (like "hello").
    # TypeError when given value is of a non-convertable type
    #   typically an object without either __int__ magic method
    #   to use with the int typecasting function, or __index__
    #   magic method which must directly return an int.
    except (ValueError, TypeError):
        return False

# If value is an integer, print it and return True.
# Otherwise, return False.
# You have to implement error catching.
# You are not allowed to use external modules
# You are not allowed to use the builtin function
#   allowing to test the nature of the variable
