class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1

        while left <= right:
            if s[left] != s[right]:
                s1 = s[:left]+s[left+1:]
                s2 = s[:right] + s[right+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            left += 1
            right -= 1
            
        return True