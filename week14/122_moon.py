class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        
        min_price = sys.maxsize
        for i in range(1, n + 1):

            if min_price < prices[i - 1]:
                # 최소 가격이 현재 가격보다 작으면
                # min_price = min(min_price, prices[i - 1])
                curr = prices[i - 1] - min_price
                # min_price = prices[i - 1]
            else:
                curr = 0
            min_price = prices[i - 1]

            dp[i] = max(dp[i - 1], dp[i - 1] + curr)
        
        return dp[n]