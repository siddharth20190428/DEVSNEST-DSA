"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.


-------------------
Constraints
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


def inorderTraversal(root):
    # recursive
    res = []
    inorder(root, res)
    return res

    """
    # iterative
    res = []
    stack = []
    curr = root
    while curr or len(stack) > 0:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
    """


def inorder(root, res):
    if root:
        if root.left:
            inorder(root.left, res)
        res.append(root.val)
        if root.right:
            inorder(root.right, res)


root = [1, None, 2, 3]
# root = []
# root = [1]
# root = [1,2]
# root = [1,None,2]