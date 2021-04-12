"""
Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].

--------------------
Constraints
0 <= num <= 10^5


Follow up:

-> It is very easy to come up with a solution with run time O(32n). Can you do it in linear time O(n) and possibly in a single pass?
-> Could you solve it in O(n) space complexity?
-> Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""


def countBits(num):
    # Time O(n^2)
    ans = []

    for n in range(num):
        s = 0
        while n != 0:
            s += 1
            n &= n - 1
        ans.append(s)
    return ans


num = 2
num = 5

print(countBits(num))