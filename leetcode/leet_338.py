# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10


class Solution:
    @staticmethod
    def bitcount(num):
        return bin(num)[2:].count("1")

    def countBits(self, n: int) -> List[int]:
        bitcount_list = [-1] * 100000
        out = []
        for i in range(n + 1):
            bc = -1
            if bitcount_list[i] == -1:
                bc = self.bitcount(i)  # this is a function which might take time
                bitcount_list.append(bc)
            else:
                bc = bitcount_list[i]  # O(1)
            out.append(bc)
        return out
