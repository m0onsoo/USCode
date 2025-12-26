class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            digit = x % 10
            x //= 10

            res = res * 10 + digit

        res *= sign

        if res > INT_MAX or res * -1 < INT_MIN:
            return 0
        return res