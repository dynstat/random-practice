# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Condition : To reduce the Space complexity to O(1)
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
s_out = ""
for idx in range(len(indices)):
    for i, val in enumerate(indices):
        if val == idx:
            s_out += s[i]

print(s_out)
