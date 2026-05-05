#!/usr/bin/env python3
best_score = __import__('best_score').best_score

scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
print(best_score(scores))
print(best_score(None))
my_dict = { 'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16 }
print(best_score(my_dict))
other_dict = { 'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Best': 20, 'PasBest': 3 }
print(best_score(other_dict))
final_dict =  { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
print(best_score(final_dict))
