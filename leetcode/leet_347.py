# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Solution:
    def topKFrequent(self, nums, k: int):
        mapcount = {}
        ans = []
        for i in nums:
            try:
                mapcount[i] += 1
            except:
                mapcount[i] = 1
        box = ["x"] * (len(nums) + 1)

        for num, num_count in mapcount.items():
            try:
                box[num_count].append(num)
            except:
                box[num_count] = [num]

        for i in box[::-1]:
            if len(ans) < k and type(i) is list:
                for n in i:
                    ans.append(n)

        print(ans)
        return ans


if __name__ == "__main__":
    nums = [1]
    nums = [1, 2]
    nums = [1, 1, 1, 2, 2, 3]
    nums = [-1, -1]

    k = 1
    obj = Solution()
    obj.topKFrequent(nums, k)
