###main tip 
### dp[x] = min( dp[x - coin] + 1 )
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1               # 만들 수 없음을 나타내는 큰 값
        dp = [0] + [INF] * amount      # dp[x] = 금액 x의 최소 동전 개수

        for x in range(1, amount + 1):
            for c in coins:
                if c <= x and dp[x - c] + 1 < dp[x]:
                    dp[x] = dp[x - c] + 1

        return -1 if dp[amount] == INF else dp[amount]