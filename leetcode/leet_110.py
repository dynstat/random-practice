# 110. Balanced Binary Tree
# Easy
# 9.1K
# 514
# Companies
# Given a binary tree, determine if it is
# height-balanced
# Height-Balanced
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# .


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True

    def rec(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        l = self.rec(root.left)
        r = self.rec(root.right)

        if (l - r) > 1 or (r - l) > 1:
            self.ans = False

        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.rec(root)
        return self.ans
