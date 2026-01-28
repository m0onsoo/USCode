from collections import Counter

# 3ms, 19.49MB
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter