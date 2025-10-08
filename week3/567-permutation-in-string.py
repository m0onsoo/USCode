# https://leetcode.com/problems/permutation-in-string/
# 567-permutation-in-string


# Brute force
## check all possible substring with all possible permutation in s1
## -> s2^2 * s1!


from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        print(s1_count)
        s2_count = defaultdict(int)

        if len(s1) > len(s2):
            return False

        l = -len(s1) + 1
        for r, char in enumerate(s2):
            if char in s1_count:
                # print(l, r, char)
                s2_count[char] += 1
                flag = True
                for ch in s1_count:
                    # print("flag", ch, s1_count[ch], s2_count[ch])
                    if s1_count[ch] != s2_count[ch]:
                        flag = False
                if flag == True:
                    return flag
            if l >= 0:
                # print("minus", l, s2[l])
                s2_count[s2[l]] -= 1
            l += 1

        return False


# from collections import Counter

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n, m = len(s1), len(s2)
#         if n > m:
#             return False

#         s1_count = Counter(s1)
#         window = Counter(s2[:n])

#         if window == s1_count:
#             return True

#         for i in range(n, m):
#             window[s2[i]] += 1
#             window[s2[i - n]] -= 1

#             # Clean up to keep the dict size small
#             if window[s2[i - n]] == 0:
#                 del window[s2[i - n]]

#             if window == s1_count:
#                 return True

#         return False
