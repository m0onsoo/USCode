# 95ms, 23.9MB

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        def isPalindrome(l, r):
            if l >= r:
                return True
            if s[l] == s[r]:
                return isPalindrome(l+1, r-1)
            
            return False
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                # 양 끝이 같은 경우 포인터 이동
                l += 1
                r -= 1
            else:
                # 양 끝이 처음 달라지는 지점부터 subset이 팰린드롬 여부인지 판별
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)

        if s[l] == s[r]:
            return True
        else:
            return False