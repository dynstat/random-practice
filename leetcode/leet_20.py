# 20. Valid Parentheses
# Easy
# 20K
# 1.2K
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


s = "( [ ( ) ] ) { h h h }"
s = "([)]"


# def valid(s):
#     d = {
#         "(": ")",
#         "{": "}",
#         "[": "]",
#     }

#     open_list = []
#     closed_list = []
#     for ch in s:
#         if ch in d:
#             open_list.append(ch)
#         elif ch in d.values():
#             closed_list.append(ch)
#         else:
#             continue
#     if len(open_list) != len(closed_list):
#         return False
#     for idx in range(len(open_list)):
#         open_bracket = open_list[idx]
#         closed_bracket = closed_list[idx]

#         if closed_bracket != d[open_bracket]:
#             return False

#     return True

s = "( [ ( ) ] ) { h h h }"
s = "([)]"


def valid(s):
    dic = {")": "(", "}": "{", "]": "["}
    stack = []
    try:
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic:
                close = dic[i]
                top = stack[-1]
                if close == top:
                    stack.pop()
                else:
                    return False
    except:
        return False
    if not stack:
        return True
    else:
        return False


print(valid(s))
