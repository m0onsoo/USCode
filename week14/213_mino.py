class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = nums[0]
        dp1[1] = max(dp1[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], nums[i]+dp1[i-2])
        dp1[n-1] = dp1[n-2]
        
        dp2[1] = nums[1]
        dp2[2] = max(dp2[1], nums[2])
        for i in range(3,n):
            dp2[i] = max(dp2[i-1], nums[i]+dp2[i-2])
        
        return max(dp1[n-1], dp2[n-1])
        