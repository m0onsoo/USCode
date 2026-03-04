# https://leetcode.com/problems/find-all-anagrams-in-a-string/


# l = 0, r = len(p)
# count_p = Counter(p)
# count_window = 

#  if count_p == count_window
# ans.append(l)

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_p = len(p)
        left_pointer = 0

        count_p = Counter(p)
        count_window = Counter(s[0:length_p])

        ans = []

        if count_p == count_window:
            ans.append(left_pointer)
        for right_pointer in range(length_p, len(s)):
            count_window[s[right_pointer]] += 1
            count_window[s[left_pointer]] -= 1
            left_pointer += 1
            if count_window == count_p:
                ans.append(left_pointer)

        return ans