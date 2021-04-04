"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

-> Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
-> In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.


--------------
Constraints
The input must be a binary string of length 32.

"""


def hammingWeight(n):
    # Loop and flip ||| Time O(n) Space O(1)
    # bits, mask = 0, 1

    # for _ in range(32):
    #     if (n & mask) != 0:
    #         bits += 1
    #     mask <<= 1

    # return bits

    # Bit Manipulation ||| Time O(1) Space O(1)
    s = 0

    while n != 0:
        s += 1
        n &= n - 1

    return s


n = 0b00000000000000000000000000001011
n = 0b00000000000000000000000010000000
n = 0b11111111111111111111111111111101

print(hammingWeight(n))