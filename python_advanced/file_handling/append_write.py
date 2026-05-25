#!/usr/bin/env python3
"""Simple example of file read in Python"""


def append_write(filename="", text=""):
    """Appends text to file, creating it beforehand if necessary"""

    count__chars_to_write = len(text)
    count__chars_written = 0
    # print(f"@dev: text to print is {count__chars_to_write}")
    # Using 'a' is like 'w' (automatic creation of file if not exist)
    #   only difference being text is added on new lines after existing content
    with open(filename, 'a', encoding="utf-8") as f:
        # print(f"@dev: file object attributes & methods: \n{dir(f)}")
        try:
            count__chars_written = f.write(text)
            # print(f"@dev chars actually written: {count__chars_written}")
        except OSError as e:
            print(e)
    return count__chars_written


if __name__ == "__main__":
    print("=== MINIMAL SELF-TEST: Start ===")
    test_filename = "my_ninja_text.tmp"

    first_line = "Hello there, I'm a ninja\n"
    second_line = "I'll disappear in just a second\n"

    print(f"We'll try to create the following file: {test_filename}")
    print(f"  with the following content... \n---")
    print(first_line, second_line, "---", sep="\n")

    print(f"Preexisting content in {test_filename}?")
    with open(test_filename, 'r') as f:
        print(f.read())

    l1_success = len(first_line) == append_write(test_filename, first_line)
    print("1st append Success :)" if l1_success else "1st append Failed!")

    l2_success = len(second_line) == append_write(test_filename, second_line)
    print("2nd append Success :)" if l1_success else "2nd append Failed!")

    print("\n--- Final content of the file: ---\n")
    with open(test_filename) as f:
        print(f.read())

    print(f"Removing all existing content of {test_filename}")
    # CANNOT WORK simply because r+ does not "empty existing",
    #   it just puts the cursor at file start.
    # Either use 'r+' with file.truncate(number_of_bytes_to_keep)
    # OR use 'w' mode which immediately removes everything.
    with open(test_filename, 'r+') as f:
        f.truncate(0)
        # f.write("") DOES NOT WORK.
        # Actually does NOT behave as intended because reads in memory
        print(f"File content should now be empty:", f.read())

    print(f"\nPLEASE DO NOT FORGET TO MANUALLY REMOVE {test_filename}")
    print("As exercise requirements prevent script for doing so automatically")
    print("  since imports are forbidden (so no os.remove(pathtofile))")

    print("=== MINIMAL SELF-TEST: END ===")
