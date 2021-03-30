"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

---------------
Constraints
1 <= S.length <= 20000
S consists only of English lowercase letters.

"""


def removeDuplicates(S):
    stack = []

    for c in S:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


s = "abbaca"

print(removeDuplicates(s))