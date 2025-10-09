from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, 1
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