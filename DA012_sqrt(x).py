"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

----------------
Constraints
0 <= x <= 2^31 - 1

"""


def mySqrt(x):
    start = 0
    end = x
    ans = start
    while start <= end:
        mid = (start + end) // 2
        if mid * mid <= x:
            start = mid + 1
            ans = mid  # as the mid is always integer, ans will eventually hold int(sqrt(x))
        else:
            end = mid - 1
    return ans


x = 4
# x=8


print(mySqrt(x))