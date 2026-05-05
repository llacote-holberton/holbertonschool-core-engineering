#!/usr/bin/env python3
common_elements = __import__('common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
# Should print ['C']
print(sorted(list(common_elements(set_1, set_2))))

set_1 = {"Chocolate", "Banana", "Vanilla Ice Cream", "Peanuts"}
set_2 = {"Chocolate", "Vanilla ice cream", "Peanuets", "Peanuts"}
# Should print ['Chocolate', 'Peanuts']
print(sorted(list(common_elements(set_1, set_2))))
