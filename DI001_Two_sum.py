"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

--------------
Constraints
2 <= nums.length <= 10^3
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""


def twoSum(nums, target):
    num_map = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in num_map:
            return [num_map[target - num], i]
        num_map[num] = i


nums = [2, 7, 11, 15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6

print(twoSum(nums, target))