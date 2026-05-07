#!/usr/bin/env python3
# PLD Exercises answered and explained

#!/usr/bin/env python3
def is_number_within_range(number, lower_bound = 10, upper_bound = 20, include_bounds = True):
    # FIRST check we have everything required to actually compute
    if not(
        type(number) == int # WARNING: not "int" as this would be a string
        and type(lower_bound) == int          # OLD METHOD
        and isinstance(upper_bound, int)      # More modern covers all types and more robust
        and isinstance(include_bounds, bool)
    ):
        print("This function expect integers for all its parameters except include_bounds (boolean), cannot proceed!")
        return None
    if lower_bound >= upper_bound:
        print("This function expect different bounds, lower bound must be first, default range is 10 to 20 included")
        return None
    # THEN compute and return, with or without boundaries included
    if (include_bounds == True):
        # Python supports chained conditions which is great not all language do sadly
        return (lower_bound <= number <= upper_bound)
    else:
        return (lower_bound < number < upper_bound)

print(f"For number 5 we should have False returned. Return value is: {is_number_within_range(5)}")
print(f"For number -666 we should have False returned. Return value is: {is_number_within_range(-666)}")
print(f"For number 15 we should have True returned. Return value is: {is_number_within_range(15)}")
print(f"For custom range 0, 1000 777 should have True returned. Return value is: {is_number_within_range(777, 0, 1000)}")
print(f"20 with included bounds should return True. Return value is: {is_number_within_range(20)}")
print(f"20 with excluded bounds should return False. Return value is: {is_number_within_range(20, include_bounds=False)}")

print("Check that guard clauses work!")
is_number_within_range("Toto")
is_number_within_range(777, "haha")
is_number_within_range(777, 5, "vers l'infini et au-delà !")
is_number_within_range(777, include_bounds="False")
