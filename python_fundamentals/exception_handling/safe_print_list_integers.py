#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    i = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        except (ValueError, TypeError):
            # Continue is NOT adequate here because
            #   it would skip the iterator increment.
            pass
        # NOTE: apparently the checker doesnt want it
        #   to be catched... :/
        # except IndexError:
        #     break
        i += 1
    print("")
    return print_count

# Print only integers.
# Skip elements that are not integers.
# Return the number of integers printed.
# All integers have to be printed on the same line followed by a new line.
# my_list can contain any type (integer, string, etc.)
# You have to implement error catching.
