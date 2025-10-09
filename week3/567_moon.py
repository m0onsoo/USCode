from collections import Counter

# 1071ms, 17.60MB
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_set = Counter(s1)

        for i in range(len(s2) - k + 1):
            window = s2[i:i+k]

            if s1_set == Counter(window):
                # print(window)
                return True
        
        return False