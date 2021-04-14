"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

-----------------
Constraints
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100

"""

from DI015_Trees import TreeNode


def maxDepth(root):
    if not root:
        return 0
    lh, rh = maxDepth(root.left), maxDepth(root.right)
    return max(lh, rh) + 1


root = [3, 9, 20, None, None, 15, 7]
root = [1, None, 2]
root = []
root = [0]
