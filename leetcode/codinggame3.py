# You are given two strings a and b such that b appears as a subsequence of a exactly once.

# You have to output the deletion string d. That is, d should be the same as a, but where only the subsequence b is kept and all other characters are replaced with -.
# Input
# Line 1: A string a.
# Line 2: A string b.
# Output
# The deletion string d of a and b.
# Constraints
# 1 <= length(b) < length(a) <= 10**3
# 1 <= length(a) * length(b) <= 6 * 10**5

# Example

# Input
# abcdef
# abef
# Output
# ab--ef

# Input
# hellothere
# hello
# Output
# hello-----

a = "hellothere"
b = "hello"
# a = "abcdef"
# b = "abef"
bl = list(b)

out = ""
for i in a:
    if i in bl:
        out += i
        bl.remove(i)
    else:
        out += "-"


print(out)
