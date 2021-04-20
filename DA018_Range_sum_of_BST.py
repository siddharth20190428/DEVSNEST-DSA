"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

---------------
Constraints
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.
"""


def dll(root):
    if not root:
        return None, None
    lh, lt = dll(root.left)
    rh, rt = dll(root.right)

    if lh:
        h = lh
        lt.right = root
        root.left = lt
    else:
        h = root

    if rh:
        t = rt
        rh.left = root
        root.right = rh
    else:
        t = root

    return h, t


def rangeSumBST(root, low, high):
    if not root:
        return 0
    elif root.val >= low and root.val <= high:
        return (
            root.val
            + rangeSumBST(root.left, low, high)
            + rangeSumBST(root.right, low, high)
        )
    elif root.val < low:
        return rangeSumBST(root.right, low, high)
    elif root.val > high:
        return rangeSumBST(root.left, low, high)


root = [10, 5, 15, 3, 7, None, 18]
low = 7
high = 15
# root = [10,5,15,3,7,13,18,1,None,6]
# low = 6
# high = 10