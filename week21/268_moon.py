
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        total = sum(num for num in range(N + 1))

        for num in nums:
            total -= num
        
        return total