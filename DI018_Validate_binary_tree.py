"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

-----------------
Constraints
The number of nodes in the tree is in the range [1, 10^4].
-23^1 <= Node.val <= 23^1 - 1
"""

from DI015_Trees import TreeNode


def check(root, low, high):
    if not root:
        return True
    v = root.val

    return (
        v > low and v < high and check(root.left, low, v) and check(root.right, v, high)
    )


def isValidBST(root):
    inf = 2 ** 31 + 1

    return check(root, -inf, inf)


root = [2, 1, 3]
root = [5, 1, 4, None, None, 3, 6]
