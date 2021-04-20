"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

-------------------
Constraints
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""


def inor(root, res):
    if root:
        if root.left:
            inor(root.left, res)
        res.append(root.val)
        if root.right:
            inor(root.right, res)
    return res


def kthSmallest(root, k):
    inord = inor(root, [])
    return inord[k - 1]


root = [3, 1, 4, None, 2]
k = 1
# root = [5,3,6,2,4,None,None,1]
# k = 3