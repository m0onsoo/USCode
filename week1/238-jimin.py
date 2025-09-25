# https://leetcode.com/problems/product-of-array-except-self/
# 238-product-of-array-except-self

# Idea :
# 1. Brute Force :
## use nested loop except for the index to mult for the rest
## n^2

# 2. Optimized:
## What if I mult all together and divide each elem?
## -> in the desc, said to not use div.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, 1
        left = []
        results = []

        for i in range(len(nums)):
            # add the product of nums[:i - 1] to i th index
            results.append(l)
            l *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            # update the element of i th index to product of results[i] * nums[i + 1:]
            results[i] *= r
            r *= nums[i]

        return results
