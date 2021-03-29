"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

---------------
Constraints
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


def threeSum(nums):
    result = []

    nums.sort()

    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x - 1]:
            continue

        y = x + 1
        z = len(nums) - 1

        required_sum = -nums[x]

        while y < z:
            current_sum = nums[y] + nums[z]

            if current_sum < required_sum:
                y += 1
            elif current_sum > required_sum:
                z -= 1
            else:
                result.append([nums[x], nums[y], nums[z]])
                y += 1
                while y < z and nums[y] == nums[y - 1]:
                    y += 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
# nums = []
# nums = [0]

print(threeSum(nums))