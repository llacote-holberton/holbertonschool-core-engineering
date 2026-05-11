#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    i = 0
    printed_count = 0
    while (i < x):
        try:
            print(my_list[i], end="")
            printed_count += 1
        # CANNOT HAPPEN with built-in types as they all implement a method
        #  __str__ which returns a "string representation" of the variable.
        except ValueError:
            pass
        except IndexError:
            # "Pass" is NOT optimal HERE.
            # Because how the code is written
            #   (traversing a list in a linear, step 1 growing order)
            #   implies that the first IndexError found necesserally
            #   means that we reached and went beyond the list limit.
            # So we can and should break to avoid additional iterations
            #   which, from deduction, would not work.
            # However in other contexts (like random access)
            #   we couldn't make this kind of deduction
            #   so then 'pass' would be adequate.
            break
        i += 1
    print("")
    return printed_count

# my_list can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.
# x represents the number of elements to print
# x can be bigger than the length of my_list
# Returns the real number of elements printed
# You have to use try: / except:
# You are not allowed to import any module
# You are not allowed to use len function
# Unless explicitly stated, do not use broad catch blocks.
