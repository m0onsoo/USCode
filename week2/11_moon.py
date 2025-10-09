from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        stored = 0
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            stored = max(stored, current)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 
        
        return stored