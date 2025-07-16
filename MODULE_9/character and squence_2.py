# characters and character squence 

# * - 0 or more occurrences of the preceding element
# + - 1 or more occurrences of the preceding element
# ? - 0 or 1 occurrence of the preceding element
# ( - start of a group
# ) - end of a group
# [ - start of a character class
# ] - end of a character class
# { - start of a quantifier
# } - end of a quantifier
# | - OR operator


import re
string = "Hello, my phone number is 123-456-7890."

pattern = "^ m,*"

print(re.findall(pattern, string))  # Output: ['num']