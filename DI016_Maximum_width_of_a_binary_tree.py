"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

-----------------
Constraints
The given binary tree will have between 1 and 3000 nodes.

"""

from DI015_Trees import TreeNode


def getw(root, rootlevel, rootindex, widthmap):
    if root:
        if rootlevel not in widthmap:
            widthmap[rootlevel] = [rootindex, rootindex]
        elif rootindex < widthmap[rootlevel][0]:
            widthmap[rootlevel][0] = rootindex
        elif rootindex > widthmap[rootlevel][1]:
            widthmap[rootlevel][1] = rootindex
        getw(root.left, rootlevel + 1, (2 * rootindex) + 1, widthmap)
        getw(root.right, rootlevel + 1, (2 * rootindex) + 2, widthmap)


def widthOfBinaryTree(root):
    widthmap = {}
    getw(root, 0, 0, widthmap)
    return max([1 + x[1] - x[0] for x in widthmap.values()])
