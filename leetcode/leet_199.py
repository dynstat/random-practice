# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        filled_idx = 0
        if root is not None:
            ans = [root.val]
            filled_idx += 1

        def rr(root, lvl=2):
            nonlocal filled_idx
            if root is None:
                return
            if root.right is not None:
                if lvl > filled_idx:
                    ans.append(root.right.val)
                    filled_idx += 1

            elif root.left is not None:
                if lvl > filled_idx:
                    ans.append(root.left.val)
                    filled_idx += 1

            rr(root.right, (lvl + 1))
            rr(root.left, (lvl + 1))

        rr(root)
        return ans
