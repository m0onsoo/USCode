# https://leetcode.com/problems/house-robber/
# 198-house-robber

# Brute force
# - 모든 경우의 수를 본다면 O(2^n)에 근접해질것.

# DP
# dp[i] = max(dp[i-2] + m(i), dp[i-1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        if len(nums) > 0:
            dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[len(nums)]
