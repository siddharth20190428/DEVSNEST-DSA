"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


-----------------
Constraints
The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000

"""

from DI015_Trees import TreeNode


def minDepth(root):
    if not root:
        return 0

    if not root.left:
        if not root.right:
            return 1
        return 1 + minDepth(root.right)

    if not root.right:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))


root = [3, 9, 20, None, None, 15, 7]
root = [2, None, 3, None, 4, None, 5, None, 6]
