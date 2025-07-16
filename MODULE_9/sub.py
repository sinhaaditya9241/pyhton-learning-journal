# sub (pattern, repl, string, count, flags)

import re
string = "it is a dog"
patern = "dog"
re.sub(patern, "cat", string, count=0, flags=0)
print(re.sub(patern, "cat", string, count=0, flags=0))

