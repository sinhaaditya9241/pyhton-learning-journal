# charater and characte squence 

# [] - empty list
# [1, 2, 3] - list of integers
# ['a', 'b', 'c'] - list of characters
# ['a', 1, 2.5] - list of mixed data types
# ['a', 'b', 'c', 1, 2.5] - list
# ['a', 'b', 'c', 1, 2.5, True]
# ['a', 'b', 'c', 1, 2.5, True,
#  None] - list of mixed data types


import re

string = "pyhton"
pattern = "[aeiou]"

print(re.findall(pattern, string, flags= 0))  # Output: ['o']