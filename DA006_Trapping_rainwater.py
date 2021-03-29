"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---------------
Constraints
n == height.length
0 <= n <= 3 * 10^4
0 <= height[i] <= 10^5

"""


def trap(height):
    n = len(height)
    if n == 0:
        return 0
    left = [height[0]]
    for i in range(1, n):
        left.append(max(left[i - 1], height[i]))

    right = [height[-1]]
    for i in range(-2, -n - 1, -1):
        right.append(max(right[-1], height[i]))
    right = right[::-1]

    ans = 0
    for i in range(n):
        ans += min(left[i], right[i]) - height[i]

    return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4,2,0,3,2,5]

print(trap(height))