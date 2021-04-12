"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

-----------
Constraints
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters
"""


def isAnagram(s, t):
    sm = {}

    for c in s:
        if c not in sm:
            sm[c] = 1
        else:
            sm[c] += 1
    for c in t:
        if c not in sm.keys():
            return False
        else:
            sm[c] -= 1
            if sm[c] == 0:
                del sm[c]
    return len(sm) == 0


s = "anagram"
t = "nagaram"

# s = "rat"
# t = "car"


print(isAnagram(s, t))
