"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

-------------
Constraints
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


def containsDuplicate(nums):
    if len(set(nums)) < len(nums):
        return True
    return False


nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(containsDuplicate(nums))