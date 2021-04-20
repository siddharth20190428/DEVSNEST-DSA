"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

-----------------------
Constraints
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

"""

from DI015_Trees import TreeNode


def lowestCommonAncestor(root, p, q):
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)

    return root


root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p = 2
q = 8
# root = [6,2,8,0,4,7,9,None,None,3,5]
# p = 2
# q = 4
# root = [2,1]
# p = 2
# q = 1