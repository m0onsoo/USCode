class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        #dp[1] = 0, dp[2] = 1, dp[3] = 1, dp[4] = dp[2], dp[5] = (2,3), (3,2)
        for coin in coins:
            for i in range(coin, amount+1): # 1,
                if i-coin >= 0:
                    dp[i] += dp[i-coin]
            
        return dp[amount]