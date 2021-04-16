"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

--------------------
Constraints
The number of nodes in the tree is in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5
"""

from DI015_Trees import TreeNode


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


def findTarget(root, k):
    h, t = dll(root)

    while h.val != t.val:
        s = h.val + t.val

        if s < k:
            h = h.right
        elif s > k:
            t = t.left
        else:
            return True
    return False


root = [5, 3, 6, 2, 4, None, 7]
k = 9
# root = [5, 3, 6, 2, 4, None, 7]
# k = 28
# root = [2, 1, 3]
# k = 4
# root = [2, 1, 3]
# k = 1
# root = [2, 1, 3]
# k = 3