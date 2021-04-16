"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

-------------------
Constraints
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.

"""
from DI015_Trees import TreeNode


def sortedArrayToBST(nums):
    length = len(nums)
    if length == 0:
        return None
    half = length // 2
    root = TreeNode(nums[half])

    root.left = sortedArrayToBST(nums[:half])
    root.right = sortedArrayToBST(nums[half + 1 :])

    return root


nums = [-10, -3, 0, 5, 9]
# nums = [1,3]