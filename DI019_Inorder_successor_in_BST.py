"""
Given a BST, and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.

------------------
Constraints
1 <= N <= 1000, where N is number of nodes
"""


def inorderSuccessor(root, x):
    if not root:
        return None

    if root.data == x.data:
        curr = root.right

        if not curr:
            return curr

        while curr.left:
            curr = curr.left

        return curr

    if root.data > x.data:
        ans = inorderSuccessor(root.left, x)
        return ans if ans else root

    return inorderSuccessor(root.right, x)


root = [1, 2, 3]
# root = [4, 8, 10, 12, 14, 20, 22]