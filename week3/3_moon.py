from collections import Counter

# Time Limit Exceeded with Brute Force approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle edge case
        if len(s) == 0:
            return 0

        for k in range(len(s), 0, -1):
            for i in range(len(s) - k + 1):
                counter = Counter(s[i:i+k])
                if counter.most_common(1)[0][1] == 1:
                    # if most common character appears only once, return the length of the substring
                    return len(counter)