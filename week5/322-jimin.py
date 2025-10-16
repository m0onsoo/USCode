# https://leetcode.com/problems/coin-change/
# 322-coin-change

# Brute force
## try every combination


# DP
## dp[i] = min(dp[i - 1] + 1, dp[i-2] + 1, dp[i-5] + 1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        for i in range(amount + 1):  # outer: target amount
            for coin in coins:  # inner: each coin
                dp_temp = amount + 1
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == (amount + 1) else dp[amount]
