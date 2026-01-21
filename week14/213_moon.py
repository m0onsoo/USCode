class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        dp1[1] = nums[0]
        for i in range(2, n):
            # 제일 앞을 포함하고 마지막을 포함하지 않는 경우
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i-1])
        
        for i in range(2, n + 1):
            # 제일 앞을 포함하지 않고 마지막을 포함하는 경우
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i-1])
        
        return max(dp1[n-1], dp2[n])