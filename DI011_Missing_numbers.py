"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

---------------
Constraints
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

"""


def missingNumber(nums):
    x = len(nums)
    for i in range(len(nums)):
        x = x ^ nums[i]
        x = x ^ i

    return x


nums = [3, 0, 1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
# nums = [0]

print(missingNumber(nums))