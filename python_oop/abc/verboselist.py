#!/usr/bin/env python3
"""Module illustrating inheritance to extend features"""


class VerboseList(list):
    """List notifying of every change on list"""

    # No need to override __init__ since we have no need
    #   for specific process at instanciation

    def append(self, item):
        """Add one element at the end of list"""
        # Super() basically forces the code to call
        # the method of the parent class
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Add n elements at the end of list"""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Removed element found by value from the list"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    # Do NOT forget to put a default value "from the start"
    def pop(self, index=-1):
        """Extract the last item from the list"""

        # NOTE: start by getting item from the index
        # NOTE: I keep the check on argument type seems fair
        if (index is None or not isinstance(index, int)):
            index = -1
        item = self[index]
        print(f"Popped [{item}] from the list.")
        super().pop(index)


# Create a class named VerboseList that extends the Python list class.
# This custom class should print a notification message every time...
#   * an item is added (using the append or extend methods)
#   * or removed (using the remove or pop methods).


if __name__ == "__main__":
    newVerboseList = VerboseList('hello', 777, True)
