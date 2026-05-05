#!/usr/bin/env python3
best_score = __import__('best_score').best_score

scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
print(best_score(scores))
print(best_score(None))
