"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---------------
Constraints
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

from DI015_Trees import TreeNode


def lowestCommonAncestor(root, p, q):
    if not root:
        return 0
    if root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    return root if left and right else left or right


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
# root = [3,5,1,6,2,0,8,None,None,7,4]
# p = 5
# q = 4
# root = [1,2]
# p = 1
# q = 2