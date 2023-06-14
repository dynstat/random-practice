# 104. Maximum Depth of Binary Tree
# Easy
# 10.9K
# 175
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        c1 = self.maxDepth(root.left)
        c2 = self.maxDepth(root.right)

        return max(c1, c2) + 1
