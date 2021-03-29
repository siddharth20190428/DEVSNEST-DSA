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