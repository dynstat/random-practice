# You are a developer concerned with security and you want to protect your data.
# You decide to set up a password for each file in your project.
# In case you forget the password of the files, you will create an algorithm allowing you to find the password of the file in question.

# Here it is, for each character of your file name:

# - If it is a number, multiply by the full length of the file name.
# - If it is a letter, calculate the remainder resulting from the ascii code of the letter divided by the full length of the file name.

# - If it is a special character, add the character index (0-based) with the full length of the file name

# - Finally, concatenate all the digits found
# Input
# Line 1 : Integer n, the number of files in the project
# Next n lines : String file, name of file
# Output
# n lines
# One line per password found
# Constraints
# 0 < n < 10
# 5 < length of file < 50

# Example
# Input
# 1
# test.py
# Output
# 43341102
