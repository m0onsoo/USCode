# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    # 잘못된 풀이
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return True

        l, r = 0, n - 1

        deleted = False
        while l < r:
            if s[l] != s[r]:
                if deleted == True:
                    print(s[l], s[r], l,r)
                    return False
                if s[l+1] == s[r]:
                    deleted = True
                    l += 2
                    r -= 1
                elif s[l] == s[r-1]:
                    deleted = True
                    l += 1
                    r -= 2
                else:
                    print(s[l], s[r], l,r)
                    return False
            else:
                l += 1
                r -= 1
        return True

    def isPal(self, string):
        n = len(string)
        if n <= 1:
            return True
        l, r = 0, n - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return True

        
        l, r = 0, n - 1

        while l < r:
            if s[l] != s[r]:
                if self.isPal(s[l:r]) or self.isPal(s[l+1:r+1]):
                    return True
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True

        