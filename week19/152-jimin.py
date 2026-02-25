# https://leetcode.com/problems/maximum-product-subarray/
# 152-maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 0
        prod = 1
        max_prod = float('-inf')

        for r, num in enumerate(nums):
            if num == 0:
                print(l, r, max_prod)
                while l < r-1:
                    prod /= nums[l]
                    l += 1
                    max_prod = max(prod, max_prod)
                l = r + 1
                prod = 1
                max_prod = max(0, max_prod)
                continue
            prod *= num
            max_prod = max(prod, max_prod)
        while l < r:
            prod /= nums[l]
            l += 1
            max_prod = max(prod, max_prod)

        return int(max_prod)