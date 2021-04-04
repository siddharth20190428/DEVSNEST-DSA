"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

---------------
Constraints
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


def subsetsWithDup(nums):
    if len(nums) == 1:
        return [[], [nums]]

    return [x + [nums[0]] for x in subsetsWithDup(nums[1:])]


nums = [1, 2, 2]
# nums = [0]

print(subsetsWithDup(nums))