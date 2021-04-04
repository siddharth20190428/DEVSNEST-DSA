"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

---------------
Constraints
-1000 <= a, b <= 1000

"""


def getSum(a, b):
    # For 32 bit constraints
    mask = 0b11111111111111111111111111111111
    MAX = 0b01111111111111111111111111111111

    # For constraints given in the question
    # mask = 0b1111111111
    # MAX = 0b0111110100

    if b == 0:
        return a if a <= MAX else ~(mask ^ a)
    return getSum(mask & (a ^ b), mask & ((a & b) << 1))


a = 1
b = 2

# a = 2
# b = -3

print(getSum(a, b))
