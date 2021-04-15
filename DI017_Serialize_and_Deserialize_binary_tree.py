"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

------------------
Constraints
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000

"""

from DI015_Trees import TreeNode


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "X"

    return (
        str(root.val) + "(" + serialize(root.left) + "),(" + serialize(root.right) + ")"
    )


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data == "X":
        return None

    data = data.split("(", 1)
    n = TreeNode(int(data[0]))
    data = "(" + data[1]
    count = 0

    for i in range(len(data)):
        c = data[i]

        if c == "(":
            count += 1
        elif c == ")":
            count -= 1

            if count == 0:
                n.left = deserialize(data[1:i])
                n.right = deserialize(data[i + 3 : -1])

                return n


root = [1, 2, 3, None, None, 4, 5]
# root = []
# root = [1]
# root = [1, 2]
