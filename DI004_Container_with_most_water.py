"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

------------------
Constraints
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        hl, hr = height[left], height[right]
        max_water = max(max_water, min(hl, hr) * (right - left))

        if hl >= hr:
            right -= 1
        if hr >= hl:
            left += 1
    return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1,1]
# height = [4,3,2,1,4]
# height = [1,2,1]

print(maxArea(height))