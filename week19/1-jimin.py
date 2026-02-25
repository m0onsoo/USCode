# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for i, num in enumerate(nums):
            c = target - num
            if num in comp:
                return [comp[num], i]
            comp[c] = i