# characters and character squence

# ^ - start of string
# $ - end of string
# \w - word character (alphanumeric plus underscore)
# \W - non-word character
# \d - digit (equivalent to [0-9])
# \D - not a digit (equivalent to [^0-9])
# \s - whitespace (equivalent to [ \t\n\r\f\v])
# \S - not whitespace (equivalent to [^ \t\n\r\f\v])
# \b - word boundary
# \B - not a word boundary (note: \b is not the same as \b
# \w\W\s\S\d\D
# \b and \B are used to find word boundaries and non-word boundaries respectively.


import re
string = "Hello, my name is John and I am 25 years old."

pattern = "\s"



print(re.findall(pattern, string, flags=0))