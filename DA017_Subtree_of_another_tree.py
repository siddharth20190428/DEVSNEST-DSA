"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

"""


def isSame(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False

    return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)


def isSubtree(s, t):
    if not s:
        return False

    if isSame(s, t):
        return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)


s = [3, 4, 5, 1, 2]
t = [4, 1, 2]
