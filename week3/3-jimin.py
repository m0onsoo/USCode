# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3-longest-substring-without-repeating-characters

# IDea:
## Brute force:
## search for all possible substrings -> n^2


# 아이디어
## 투 포인터 + 세트
## 만약 이미 본 캐릭터면 왼쪽 포인터 증가


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}

        temp_max = 0
        result = 0

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            temp_max = r - l + 1
            print(temp_max, r, l, char)
            seen[char] = r
            result = max(temp_max, result)

        return result
