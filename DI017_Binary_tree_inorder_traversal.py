"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


----------------
Constraints
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""
from DI015_Trees import TreeNode


def levelOrder(root):
    if not root:
        return []

    ans = [[]]
    x = "X"

    q = [root, x]

    while True:
        n = q.pop(0)

        if n == x:
            if len(q) == 0:
                return ans
            q.append(x)
            ans.append([])
        else:
            ans[-1].append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)


root = [3, 9, 20, None, None, 15, 7]
# root = [1]
# root = []