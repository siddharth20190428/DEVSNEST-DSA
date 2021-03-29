"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10^4.

"""


def characterReplacement(s, k):
    max_repeats = 0
    l = 0
    ch_freq = {}
    max_length = 0

    for r in range(len(s)):
        current = s[r]

        ch_freq[current] = ch_freq.get(current, 0) + 1
        max_repeats = max(max_repeats, ch_freq[current])

        current_length = r - l + 1
        print(current_length, max_repeats)
        if current_length - max_repeats <= k:
            max_length = max(max_length, current_length)
        else:
            ch_freq[s[l]] -= 1
            l += 1
    return max_length


s = "ABAB"
k = 2

s = "AABABBA"
k = 1

print(characterReplacement(s, k))
