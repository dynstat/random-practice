# Definition for a binary tree node.


class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1)))


def hasPathSum(self, root, targetSum: int) -> bool:
    pass
