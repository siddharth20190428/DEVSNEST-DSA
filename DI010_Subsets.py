"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

---------------
Constraints
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""


def subsets(nums):
    # Without recursion
    ans = [[]]

    for num in nums:
        ans += [x + [num] for x in ans]

    return ans


nums = [1, 2, 3]
# nums = [0]

print(subsets(nums))