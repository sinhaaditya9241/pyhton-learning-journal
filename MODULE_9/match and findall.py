
import re

pattern = "apple"
if re.match(pattern, "apple" ):
    print ("Match found")
else:
    print ("No match found")

# findall (pattern , string , flags = 0 )

import re
pattern = "apple"
string = re.findall("a", pattern)
print(string)