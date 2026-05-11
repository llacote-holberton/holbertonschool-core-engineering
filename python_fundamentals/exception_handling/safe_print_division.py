#!/usr/bin/env python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        # print("Provided divisor is 0!! Cannot divide by zero!!")
        pass
    except (ValueError, TypeError):
        # print("Either dividend ({a}) or divisor ({b})", end="")
        # print(" aren't of an exploitable type/value")
        pass
    finally:
        print(f"Inside result: {result}")
    return result

# Perform the division inside a try block.
# If any other exception occurs, print "Inside result: None".
# Always print "Inside result: <result>" using finally.
# Return the result (or None).
# .format( just for checker.
