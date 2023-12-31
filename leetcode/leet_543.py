# 543. Diameter of Binary Tree
# Easy
# 11.5K
# 719
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    ans = 0

    def d(self, root):
        if not root:
            return 0

        l = self.d(root.left)
        r = self.d(root.right)

        self.ans = max(self.ans, l + r)

        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d(root)
        return self.ans
