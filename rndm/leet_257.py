import typing


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


def binaryTreePaths(root):
    if not root:
        return None

    q = [(root, str(root.val))]
    res = []

    while q:
        node, path_upto_node = q.pop()

        if not any([node.left, node.right]):
            res.append(path_upto_node)

        else:
            q.append(
                (node.left, path_upto_node + "->" + str(node.left.val))
            ) if node.left else None
            q.append(
                (node.right, path_upto_node + "->" + str(node.right.val))
            ) if node.right else None

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print(binaryTreePaths(root))
