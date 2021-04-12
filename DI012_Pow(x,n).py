"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

------------------
Constraints
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4

"""


def myPow(x, n):
    isnneg, isxneg = n < 0, x < 0

    x, n = abs(x), abs(n)

    if n == 0:
        return 1
    if n == 1:
        return 1 / x if isnneg else x

    pwr = myPow(x, n // 2)

    ans = pwr * pwr if n % 2 == 0 else pwr * pwr * x

    if isxneg and n % 2 == 1:
        ans = -ans
    if isnneg:
        ans = 1 / ans
    return ans


x = 2.00000
n = 10
# x = 2.10000
# n = 3
# x = 2.00000
# n = -2

print(myPow(x, n))
