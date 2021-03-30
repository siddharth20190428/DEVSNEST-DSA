"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

--------------
Constraints
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

"""


def isPalindrome(s):
    l = [c.lower() for c in s if c.isalnum()]

    stack, queue = list(l), list(l)

    for i in range(len(l) // 2):
        if stack.pop() != queue.pop(0):
            return False
    return True


s = "A man, a plan, a canal: Panama"

# s = "race a car"

print(isPalindrome(s))