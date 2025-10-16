from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize array with 0
        opt = [0] * (len(nums)+1)
        opt[1] = nums[0]

        for i in range(2, len(nums)+1):
            opt[i] = max(opt[i-1], opt[i-2]+nums[i-1])
        
        return opt[-1]
        