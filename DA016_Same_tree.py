"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

-----------------
Constraints
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

"""


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    if p and q:
        return (
            p.val == q.val
            and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right)
        )


p = [1, 2, 3]
q = [1, 2, 3]
# p = [1,2]
# q = [1,null,2]
# p = [1,2,1]
# q = [1,1,2]