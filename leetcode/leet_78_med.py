# 78. Subsets
# Medium
# 14.8K
# 215
# Companies
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # bcaktracking approach
        def rec(i, subset=[]):
            # return if the index crosses the length of the nums array.
            if i >= len(nums):
                ans.append(
                    subset.copy()
                )  # since the list gets modified as the same name refers to the same list
                return

            # appending if the number exists in the list
            subset.append(nums[i])
            # doing the same on the left side, which means we chose to append the item
            rec(i + 1, subset=subset)
            # this is going to be the right side where we chose to ignore the item, in the previous subset.
            subset.pop()
            rec(i + 1, subset=subset)

        rec(0)
        return ans
