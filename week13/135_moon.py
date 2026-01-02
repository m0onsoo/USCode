# 19ms, 19.74MB

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            prev, curr = ratings[i - 1], ratings[i]
            if prev < curr:
                candies[i] = candies[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            curr, forw = ratings[i], ratings[i + 1]
            if curr > forw:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)