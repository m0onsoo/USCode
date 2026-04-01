
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum_nums = 0
        og_sum = 0
        for i, num in enumerate(nums):
            og_sum += i+1
            sum_nums += num
        return og_sum - sum_nums