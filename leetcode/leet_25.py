def removeElement(nums, val: int):
    print(nums)
    print(id(nums))
    idx_to_remove = []
    count = 0
    for idx, num in enumerate(nums):
        if num == val:
            idx_to_remove.append(idx)
            count += 1
    c = 0
    for i in idx_to_remove:
        nums.pop(i - c)
        c += 1
    print(id(nums))
    print(nums)
    return count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
removeElement(nums, val)
