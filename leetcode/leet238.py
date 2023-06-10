nums = [1, 2, 3, 4]

left = []
right = []

ans = []

t = 1
for i in nums:
    t *= i
    left.append(t)
t = 1
for i in nums[::-1]:
    t *= i
    right.append(t)
right = right[::-1]

for idx, val in enumerate(nums):
    l_idx = idx - 1
    r_idx = idx + 1

    if l_idx < 0:
        lp = 1
    else:
        lp = left[l_idx]
    if r_idx > len(nums) - 1:
        rp = 1
    else:
        rp = right[r_idx]

    p = lp * rp
    ans.append(p)
