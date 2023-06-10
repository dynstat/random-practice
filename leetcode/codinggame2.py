# You will be given a chemical formula s . You must extract the symbols of elements from the given formula. You must print the names of elements in the order they appear in the chemical formula in a single line and with each element separated by an empty space. Make sure you don't repeat the symbols of elements while printing.

# Note: In a formula like CH3COONa, the elements are C H O Na . Here Na is a single element and N and a must not be printed separately.


s = "CH3COONa"

# expected output --> C H O Na

out = ""

for elm in s:
    if elm in out:
        continue
    try:
        if elm.isupper():
            out += " "
            out += elm
        if elm.islower():
            out += elm
    except:
        pass

print(out.strip())
