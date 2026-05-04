#!/usr/bin/env python3
for number in range(0, 98+1):
    print(f"{number} = {format(number, 'x')}")
# Using +1 as upper bound is NOT included
# Even more concise:     (f'{number} = {number:x}')
