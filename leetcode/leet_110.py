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
#     def __init__(self, val=0, ):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


# class Solution:
#     ans = True

#     def rec(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return False

#         l = self.rec(root.left)
#         r = self.rec(root.right)

#         if (l - r) > 1 or (r - l) > 1:
#             self.ans = False

#         return max(l, r) + 1

#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.rec(root)
#         return self.ans


#############################################################################  testing other related stuff ########################################
# creating a Tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7, TreeNode(9), TreeNode(2))


def rec(root, ans=True):
    if not root:
        return 0, True

    l, ans = rec(root.left, ans)
    r, ans = rec(root.right, ans)

    if (l - r) > 1 or (r - l) > 1:
        ans = False

    return ((max(l, r) + 1), ans)


print(rec(root))
