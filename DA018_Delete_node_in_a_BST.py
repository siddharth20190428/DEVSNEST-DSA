"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

-----------------
Constraints
The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
"""


def justgreater(root):
    curr = root
    while curr.left:
        curr = curr.left

    return curr


def deleteNode(root, key):
    if not root:
        return None

    if root.val < key:
        root.right = deleteNode(root.right, key)
    elif root.val > key:
        root.left = deleteNode(root.left, key)

    else:
        if not root.left and not root.right:
            root = None

        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left

        else:
            temp = justgreater(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    return root


root = [5, 3, 6, 2, 4, None, 7]
key = 3
# root = [5,3,6,2,4,None,7]
# key = 0
# root = []
# key = 0