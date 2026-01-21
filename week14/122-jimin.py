# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# 122-best-time-to-buy-and-sell-stock-ii

# DP[]
# Buy/Sell, Hold

# 솔루션 봐버림...


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge cases
        if not prices:
            return 0
        prev = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            cur_price = prices[i]
            if prev < cur_price:
                ans += cur_price - prev
            prev = cur_price

        return ans


# 참고 : DP

# from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         cash = 0
#         hold = -prices[0]

#         for price in prices[1:]:
#             prev_cash = cash
#             cash = max(cash, hold + price)      # sell or do nothing
#             hold = max(hold, prev_cash - price) # buy or do nothing

#         return cash
