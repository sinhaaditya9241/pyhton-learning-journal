# search (pattern, string, flags=0)

import re
pattern = "apple"
if re.search(pattern, "ballapple", flags=0):
    print('true')

else:
    print('false')


if re.match(pattern, "ballapple", flags=0):
    print('true')

else:
    print('false')