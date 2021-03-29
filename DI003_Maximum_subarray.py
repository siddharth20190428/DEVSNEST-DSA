"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

-----------------
Constraints
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5

"""


def maxSubArray(nums):
    if max(nums) < 0:
        return max(nums)

    m, c = 0, 0

    for num in nums:
        c += num
        if c < 0:
            c = 0

        if m < c:
            m = c
    return m


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# nums = [1]

# nums = [5, 4, -1, 7, 8]
