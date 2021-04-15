"""
Given the root of a binary tree, invert the tree, and return its root.

-----------------
Constraints
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

from DI015_Trees import TreeNode


def invertTree(root):
    if root:
        if root.left or root.right:
            root.right, root.left = invertTree(root.left), invertTree(root.right)
        return root


root = [4, 2, 7, 1, 3, 6, 9]
# root = [2,1,3]
# root = []