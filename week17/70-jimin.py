# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)] # n + 1 해야함
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1): #여기도 
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]