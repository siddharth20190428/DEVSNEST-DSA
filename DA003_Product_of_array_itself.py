"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

-------------
Constraints
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


def productExceptSelf(nums):
    length = len(nums)

    left, right = [0] * length, [0] * length

    left[0], right[-1] = 1, 1

    for i in range(1, length):
        left[i] = left[i - 1] * nums[i - 1]

    for i in reversed(range(length - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    answer = []
    for i in range(length):
        answer.append(left[i] * right[i])

    return answer


nums = [1, 2, 3, 4]
# nums = [-1,1,0,-3,3]

print(productExceptSelf(nums))