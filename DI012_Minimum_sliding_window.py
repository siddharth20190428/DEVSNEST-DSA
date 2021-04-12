"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

-----------------
Constraints
1 <= s.length, t.length <= 10^5
s and t consist of English letters.

"""
import collections


def minWindow(s, t):
    tmap = collections.Counter(t)
    tcount = len(t)

    cmap = {}
    for i in tmap.keys():
        cmap[i] = 0

    ccount = 0

    l = 0
    ans = s + "!"
    for r in range(len(s)):
        c = s[r]

        if c in tmap:
            cmap[c] += 1
            if cmap[c] <= tmap[c]:
                ccount += 1

            while l < r and (s[l] not in tmap or cmap[s[l]] > tmap[s[l]]):
                if tmap[s[l]]:
                    cmap[s[l]] -= 1
                l += 1

            if tcount == ccount:
                ans = ans if len(ans) <= r - l + 1 else s[l : r + 1]
            r += 1

    return ans if len(ans) <= len(s) else ""


s = "ADOBECODEBANC"
t = "ABC"
# s = "a"
# t = "a"

print(minWindow(s, t))
