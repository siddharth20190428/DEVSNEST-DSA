"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

-------------------
Constraints
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.

"""


def gst(root, s):
    if not root:
        return s

    s = gst(root.right, s)
    root.val += s
    s = root.val

    return gst(root.left, s)


def bstToGst(root):
    gst(root, 0)

    return root


root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
# root = [0, None, 1]
# root = [1, 0, 2]
# root = [3, 2, 4, 1]
