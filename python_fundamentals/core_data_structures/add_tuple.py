#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    # CANNOT WORK as in case of a miss it ends up
    #   with one integer which isn't "unpackable"
    # m1_op1, m2_op1 = tuple_a or 0
    # print(f"\nOriginal tuples are {tuple_a} | {tuple_b}")

    # Explicit "safe unpacking" but hard to scale.
    m1_op1 = tuple_a[0] if len(tuple_a) > 0 else 0
    m2_op1 = tuple_a[1] if len(tuple_a) > 1 else 0
    # print(f"m1_op1 is {m1_op1}")
    # print(f"m2_op1 is {m2_op1}")

    # Cleaner version using "padding" to "fill up" tuple, thus
    #   ensuring at least 2 elements even if originally empty.
    # Then "cut our pick" to ensure we only get as many as we need
    #   and no more even if the source ends up with "too many members"
    m1_op2, m2_op2 = (tuple_b + (0, 0))[:2]
    # print(f"m1_op2 is {m1_op2}")
    # print(f"m2_op2 is {m2_op2}")

    m1 = m1_op1 + m1_op2
    m2 = m2_op1 + m2_op2
    result = (m1, m2)
    # print(f"Tuple of additions is: {result}")
    return result
# Return a new tuple with exactly two integers.
# Treat missing values as 0.
# Ignore values beyond the first two.
# Basically add a1 with b1 and a2 with b2
#   to form a new tuple to return
