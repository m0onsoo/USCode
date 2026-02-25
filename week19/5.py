# https://leetcode.com/problems/daily-temperatures/?envType=problem-list-v2&envId=plakya4j

# 739-daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while stack:
                prev_temp, prev_idx = stack.pop()
                if prev_temp < temp:
                    ans[prev_idx] = i - prev_idx
                else:
                    stack.append((prev_temp, prev_idx))
                    break
            stack.append((temp, i))

        
        return ans