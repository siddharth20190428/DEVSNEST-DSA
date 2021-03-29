"""
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

------------
Constraints
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""


def nextGreaterElement(nums1, nums2):
    stack = []
    hmap = {}

    hmap[nums2[-1]] = -1
    stack.append(nums2[-1])

    for i in range(len(nums2) - 2, -1, -1):
        x = nums2[i]
        if x > stack[-1]:
            while len(stack) > 0 and x > stack[-1]:
                stack.pop()
        hmap[x] = -1 if len(stack) == 0 else stack[-1]
        stack.append(x)

    res = []
    for i in nums1:
        res.append(hmap[i])

    return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

print(nextGreaterElement(nums1, nums2))
