class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        if b == 0:
            return a if a <= MAX_INT else ~(a ^ MASK)

        return self.getSum(a ^ b, (a & b) << 1)
