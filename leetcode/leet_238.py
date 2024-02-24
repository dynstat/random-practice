def productExceptSelf(nums):
    pre_product = [0 for l in range(len(nums))]
    sum_ = 1
    for idx, val in enumerate(nums):
        pre_product[idx] = sum_
        sum_ *= val
    sum_ = 1
    for idx, val in enumerate(nums[::-1]):
        c_idx = len(nums) - idx - 1
        pre_product[c_idx] *= sum_
        sum_ *= val

    print(pre_product)


productExceptSelf([1, 2, 3, 4])
productExceptSelf([-1, 1, 0, -3, 3])
