class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def levelorder(root):
    lo = [root]
    while len(lo) > 0:
        node = lo.pop(0)
        print(node.data, end=" ")
        # result.append(node.data)
        if node.left:
            lo.append(node.left)
        if node.right:
            lo.append(node.right)


def leafnodes(root):
    if root:
        if not root.left and not root.right:
            print(root.data, end=" ")
        leafnodes(root.left)
        leafnodes(root.right)


def traversals(root):
    print("in order :")
    inorder(root)
    print("\npre order :")
    preorder(root)
    print("\npost order :")
    postorder(root)
    print("\nlevel order :")
    levelorder(root)
    print("\nleaf node :")
    leafnodes(root)


root = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
)

traversals(root)