"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Note:
1.The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""


def validPalindrome(s):
    l, r = 0, len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            one, two = s[l:r], s[l + 1 : r + 1]
            return one == one[::-1] or two == two[::-1]
        l += 1
        r -= 1

    return True


s = "aba"
# s = "abca"

print(validPalindrome(s))