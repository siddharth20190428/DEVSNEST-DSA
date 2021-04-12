"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

------------------
Constraints
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

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


print("AABABBA", 1)
print("ABAB", 2)