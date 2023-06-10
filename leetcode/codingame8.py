s = "Pizyxas"
# out = "Psiazx"
out: str = ""

for i in range(len(s)):
    j = len(s) - i - 1
    if i == j:
        out += s[i]
    if i >= j:
        break

    out += s[i]
    out += s[j]
print(out)


from typing import *

x: Optional[Cat, str] = ""

x = 5
