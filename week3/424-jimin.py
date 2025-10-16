# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424-longest-repeating-character-replacement

# idea:
# brute force:
# check all possible substrings and availability -> n^3

## sliding window
## count all elements while sliding.
## if topfreq - windowsize > k -> shorten window size
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l = 0
        max_freq = 0
        ans = 0

        for r, char in enumerate(s):
            count[char] += 1
            max_freq = max(max_freq, count[char])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
