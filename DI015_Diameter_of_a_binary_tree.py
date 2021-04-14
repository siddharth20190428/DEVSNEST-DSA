"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

-----------------
Constraints
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100

"""

from DI015_Trees import TreeNode


def dia(node):
    if not node:
        return 0, 0
    lp, lw = dia(node.left)
    rp, rw = dia(node.right)

    return 1 + max(lp, rp), max(lw, rw, 1 + lp + rp)


def diameterOfBinaryTree(root):
    return dia(root)[1] - 1


root = [1, 2, 3, 4, 5]
root = [1, 2]
