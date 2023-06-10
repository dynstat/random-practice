# You are given a list of names. You must output the initials of each name, with full stops after each letter, ignoring any titles ('Dr', 'Mr', 'Mrs', 'Ms' , 'Lord', 'Lady' or 'Sir') and any degrees ('BA', 'LLB' , 'MD' or 'PhD) or other suffixes ('Jr' or 'Snr).
# Input
# An integer N for the number of names to initialise.

# Next N lines: the Names to be initialised.
# Output
# N lines with the initials of the input names.
# Constraints
# The titles will only be one of 'Dr', 'Mr', 'Mrs', 'Ms' ,
# The titles will only be one of 'Dr', 'Mr', 'Mrs', 'Ms' , 'Lord', 'Lady' or 'Sir', the degrees will only be one of 'BA', 'LLB' , 'MD' or 'PhD' and the only other possible suffixes are 'Jr' or 'Snr'
# Example
# Input
# 1
# John Smith
# Output
# J.S.

titles = {"Dr", "Mr", "Mrs", "Ms", "Lord", "Lady", "Sir"}
degrees = {"BA", "LLB", "MD", "PhD"}
suffixes = {"Jr", "Snr"}

name = "PhD Mr John Smith Jr"  # output --> J.S.

for t in titles:
    name = name.replace(f"{t} ", "")
for d in degrees:
    name = name.replace(f"{d}", "")
for s in suffixes:
    name = name.replace(f" {s}", "")

name = name.split()
out = ""
for i in name:
    out += i[0]
    out += "."

print(out)
