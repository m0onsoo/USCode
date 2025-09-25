# https://leetcode.com/problems/container-with-most-water/
# 11-container-with-most-water

# Idea:
# Brute force
## search nested loop. -> n^2 (time limit exceed)

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)

#         ans = -1
#         for i in range(n-1):
#             for j in range(i + 1, n):
#                 amount = (j - i) * min(height[i], height[j])
#                 ans = max(ans, amount)

#         return ans


# Optimize: -> still n^2

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         ans = -1
#         l = 0
#         for r, h in enumerate(height):
#             for i in range(r):
#                 amount = (r - i) * min(height[i], height[r])
#                 if amount > ans:
#                     ans = amount
#                     l = i
#                     print(ans, l, r)
#         print(l, r)
#         return ans


# Two-Pointer


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            amount = (r - l) * min(height[l], height[r])
            if amount > ans:
                ans = amount
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        return ans
