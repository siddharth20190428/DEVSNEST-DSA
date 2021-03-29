"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

-------------
Constraints
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


def isValid(s):
    if len(s) % 2 == 1:
        return False

    braces = {"[": "]", "{": "}", "(": ")"}

    stack = []

    for c in s:
        if c in braces:
            stack.append(c)
        elif len(stack) != 0 and c == braces[stack[-1]]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "{[]}"