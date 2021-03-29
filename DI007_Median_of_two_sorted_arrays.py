"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

--------------
Constraints
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""


def findMedianSortedArrays(nums1, nums2):
    median, i, j, n, m = 0, 0, 0, len(nums1), len(nums2)

    if n > m:
        nums1, nums2 = nums2, nums1
        n, m = m, n

    min_index, max_index = 0, n

    while min_index <= max_index:
        i = (min_index + max_index) // 2
        j = ((n + m + 1) // 2) - i

        if i < n and j > 0 and nums2[j - 1] > nums1[i]:
            min_index = i + 1
        elif i > 0 and j < m and nums2[j] < nums1[i - 1]:
            max_index = i - 1

        else:
            if i == 0:
                median = nums2[j - 1]
            elif j == 0:
                median = nums1[i - 1]
            else:
                median = max(nums1[i - 1], nums2[j - 1])
            break

    if (n + m) % 2 == 1:
        return median
    if i == n:
        return (median + nums2[j]) / 2
    if j == m:
        return (median + nums1[i]) / 2

    return (median + min(nums1[i], nums2[j])) / 2


nums1 = [1, 3]
nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]

nums1 = [0, 0]
nums2 = [0, 0]

nums1 = []
nums2 = [1]

nums1 = [2]
nums2 = []

print(findMedianSortedArrays(nums1, nums2))
